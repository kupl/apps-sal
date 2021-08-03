# dp[k][i] = # of ways at step k in i position

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        dp = [[0] * (steps // 2 + 2) for _ in range(steps + 1)]  # 如果k=500, i可以去到250 length 有251个
        dp[0][0] = 1
        M = 10**9 + 7

        for k in range(1, steps + 1):
            for i in range(steps // 2 + 1):
                if i == 0:
                    dp[k][i] = (dp[k - 1][i] + dp[k - 1][i + 1]) % M

                elif i == arrLen - 1:
                    dp[k][i] = (dp[k - 1][i] + dp[k - 1][i - 1]) % M

                else:
                    dp[k][i] = (dp[k - 1][i] + dp[k - 1][i - 1] + dp[k - 1][i + 1]) % M

        return dp[steps][0] % M
