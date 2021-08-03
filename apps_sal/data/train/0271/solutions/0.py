class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        can = True
        smallest_idx = n - 1

        for i in range(n - 2, -1, -1):
            can = i + nums[i] >= smallest_idx
            if can:
                smallest_idx = i
        return can
