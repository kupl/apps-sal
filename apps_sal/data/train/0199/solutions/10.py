class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        longest = 1
        current = 1

        nums.sort()

        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current += 1
                else:
                    longest = max(longest, current)
                    current = 1

        return max(longest, current)
