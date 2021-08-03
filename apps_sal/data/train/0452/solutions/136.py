class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, d + 1):
                for h in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], dp[h][j - 1] + max(jobDifficulty[h:i]))
        return dp[n][d] if dp[n][d] != float('inf') else -1
