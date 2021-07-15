class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        dp = {0: -1}
        cur = 0
        res = n = len(nums)
        for i, a in enumerate(nums):
            cur = (cur + a) % p
            dp[cur] = i
            if (cur - need) % p in dp:
                res = min(res, i - dp[(cur - need) % p])
        return res if res < n else -1
