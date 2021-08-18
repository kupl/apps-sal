class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dp = [0] * (1 + len(nums))
        mem = {0: 0}
        cur = 0
        for i, v in enumerate(nums):
            cur += v
            dp[i + 1] = dp[i]
            if cur - target in mem:
                dp[i + 1] = max(dp[i + 1], dp[mem[cur - target]] + 1)
            mem[cur] = i + 1
        return dp[-1]
