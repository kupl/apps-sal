class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps + 1)
        dp = [[0] * arrLen for _ in range(steps)]
        dp[0][0] = 1
        dp[0][1] = 1
        m = 10 ** 9 + 7
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if j == 0:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1]) % m
                elif j == len(dp[0]) - 1:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % m
                else:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1] + dp[i - 1][j - 1]) % m
        return dp[-1][0]
