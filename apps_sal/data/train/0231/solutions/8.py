class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

            if nums[i] > 0 and nums[i] != i + 1:
                j, nums[i] = nums[i], 0
                while 0 < j <= len(nums) and nums[j - 1] != j:
                    next_j = nums[j - 1]
                    nums[j - 1] = j
                    j = next_j

        for i, num in enumerate(nums):
            if not num:
                return i + 1

        if nums and nums[-1] > 0:
            return nums[-1] + 1

        return 1
