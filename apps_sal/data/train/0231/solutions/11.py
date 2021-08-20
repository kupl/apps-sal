class Solution:

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        n = len(nums)
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= n and (nums[i] != nums[nums[i] - 1]):
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp
        for j in range(len(nums)):
            if nums[j] != j + 1:
                return j + 1
        return n + 1
