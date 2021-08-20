class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        s = 0
        mod = [(s := ((s + n) % p)) for n in nums]
        total = mod[-1]
        if not total:
            return 0
        last = {0: -1}
        res = float('inf')
        for (i, n) in enumerate(mod):
            comp = (n - total) % p
            if comp in last:
                res = min(res, i - last[comp])
            last[n] = i
        return -1 if res == len(nums) else res
