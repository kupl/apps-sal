class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        right_most = min(steps + 1 // 2, arrLen)
        dp = [[0 for __ in range(right_most)] for _ in range(steps)]
        for i in range(steps):
            if i == 0:
                dp[0][0] = 1
                dp[0][1] = 1
            else:
                for j in range(right_most):
                    dp[i][j] = dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i - 1][j - 1]
                    if j < right_most - 1:
                        dp[i][j] += dp[i - 1][j + 1]
        return dp[-1][0] % (10 ** 9 + 7)
