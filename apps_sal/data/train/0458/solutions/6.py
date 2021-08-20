class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n + 1)]
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        res = prefix[n] % p
        if res == 0:
            return 0
        loc = {}
        ans = float('inf')
        for (i, pre) in enumerate(prefix):
            d = (pre - res) % p
            if d in loc:
                ans = min(ans, i - loc[d])
            loc[pre % p] = i
        return -1 if ans == float('inf') or ans == n else ans
