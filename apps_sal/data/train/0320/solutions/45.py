class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mx = 1
        ops = 0
        for nm in nums:
            bt = 0
            while nm > 0:
                ops += (nm & 1)
                bt += 1
                nm = (nm >> 1)
            mx = max(mx, bt)
        return ops + mx - 1
