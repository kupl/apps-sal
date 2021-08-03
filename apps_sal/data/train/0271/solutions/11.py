class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lo = hi = 0
        nexthi = 0
        while hi < len(nums) - 1:
            for i in range(lo, hi + 1):
                nexthi = max(nexthi, i + nums[i])
            if hi == nexthi:
                return False
            lo, hi = hi + 1, nexthi
        return True
