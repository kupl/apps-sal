class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = 0
        ss = sum(nums) % p
        if ss == 0:
            return 0
        h = {}
        h[0] = -1
        import sys
        ans = sys.maxsize
        for i, e in enumerate(nums):
            s += e
            c = (p - (ss - s) % p) % p
            if c in h:
                ans = min(ans, i - h[c])
            h[s % p] = i
        if ans == len(nums):
            ans = -1
        return ans
