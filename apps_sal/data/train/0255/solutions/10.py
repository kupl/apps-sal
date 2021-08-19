class Solution:

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        lo = 0
        hi = 0
        jumps = 0
        while hi < L - 1:
            jumps += 1
            nexthi = hi
            for i in range(lo, hi + 1):
                nexthi = max(nexthi, i + nums[i])
                if nexthi >= L - 1:
                    return jumps
            (lo, hi) = (hi + 1, nexthi)
        return jumps
