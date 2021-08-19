class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        dp = {}
        dp[0] = -1
        n = len(nums)
        res = n
        cur = 0
        for (i, num) in enumerate(nums):
            cur = (cur + num) % p
            dp[cur] = i
            if (cur - need) % p in dp:
                res = min(res, i - dp[(cur - need) % p])
        return res if res < n else -1
