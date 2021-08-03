class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps // 2 + 1)
        dp = [0] * arrLen
        dp[0] = 1
        mod = 10**9 + 7
        for i in range(steps):
            dp = [(dp[j] + (dp[j - 1] if j >= 1 else 0) + (dp[j + 1] if j + 1 < arrLen else 0)) % mod for j in range(arrLen)]
        return dp[0]
