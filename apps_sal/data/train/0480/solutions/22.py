class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        arrLen = min(steps, arrLen)
        dp = [[0] * (steps + 1) for _ in range(arrLen)]
        dp[0][0] = 1
        for j in range(1, steps + 1):
            for i in range(0, arrLen):
                dp[i][j] = dp[i][j - 1]
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j - 1]
                if (i + 1) < arrLen:
                    dp[i][j] += dp[i + 1][j - 1]
                dp[i][j] = dp[i][j] % mod
        return dp[0][-1]
