class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        M = 1000000.0
        dp = [[M] * (d + 1) for i in range(n + 1)]
        dp[n][0] = 0
        dp[n - 1][1] = jobDifficulty[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(1, d + 1):
                m = -1
                for k in range(i, n):
                    m = max(m, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], m + dp[k + 1][j - 1])
        return dp[0][d] if dp[0][d] < M else -1
