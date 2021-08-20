class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [[0 for _ in range(min(steps + 1, arrLen))] for _ in range(steps + 1)]
        dp[0][0] = 1
        for s in range(1, steps + 1):
            for i in range(min(s + 1, arrLen, steps - s + 1)):
                dp[s][i] = dp[s - 1][i] % (10 ** 9 + 7)
                if i > 0:
                    dp[s][i] += dp[s - 1][i - 1]
                if i < arrLen - 1:
                    dp[s][i] += dp[s - 1][i + 1]
        return dp[-1][0] % (10 ** 9 + 7)
