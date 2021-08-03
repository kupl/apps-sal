class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_dist = min(steps // 2 + 1, arrLen)
        dp = [[0] * (max_dist + 1) for _ in range(steps)]

        dp[0][0] = dp[0][1] = 1

        for i in range(1, steps):
            for j in range(max_dist):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]) % (10**9 + 7)

        return dp[-1][0]
