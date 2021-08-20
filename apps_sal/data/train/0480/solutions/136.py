class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        maxPos = min(steps, arrLen)
        mod = 10 ** 9 + 7
        dp = [[0] * (maxPos + 1) for _ in range(steps + 1)]
        dp[1][0] = 1
        dp[1][1] = 1
        for s in range(2, steps + 1):
            for p in range(maxPos):
                dp[s][p] = dp[s - 1][p] + dp[s - 1][p + 1]
                dp[s][p] += dp[s - 1][p - 1] if p > 0 else 0
                dp[s][p] %= mod
        return dp[steps][0]
