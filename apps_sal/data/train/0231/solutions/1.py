class Solution:

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        for index in range(len(nums)):
            while nums[index] != index + 1:
                tmp = nums[index]
                if tmp <= 0 or tmp > len(nums) or tmp == nums[tmp - 1]:
                    break
                nums[index] = nums[tmp - 1]
                nums[tmp - 1] = tmp
        for index in range(len(nums)):
            if nums[index] != index + 1:
                return index + 1
        return len(nums) + 1
