class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[0] * n] + [[float('inf')] * n for _ in range(d - 1)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, n):
            dp[0][i] = max(jobDifficulty[i], dp[0][i - 1])
        for i in range(1, d):
            for j in range(i, n):
                max_r = jobDifficulty[j]
                for r in range(j, i - 1, -1):
                    max_r = max(max_r, jobDifficulty[r])
                    dp[i][j] = min(dp[i][j], max_r + dp[i - 1][r - 1])
        return dp[-1][-1]
