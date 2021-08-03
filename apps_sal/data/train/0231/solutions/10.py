class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        for i in range(len(nums)):
            while 0 < nums[i] < len(nums) and nums[i] != i and nums[i] != nums[nums[i]]:
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
                print((temp, nums))
        for i in range(1, len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
