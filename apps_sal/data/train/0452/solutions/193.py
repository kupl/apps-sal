class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        dp = [[float('inf')] * n + [0] for i in range(d + 1)]
        for i in range(1, d + 1):
            for j in range(n - i + 1):
                maxd = 0
                for x in range(j, n - i + 1):
                    maxd = max(maxd, jobDifficulty[x])
                    dp[i][j] = min(dp[i][j], maxd + dp[i - 1][x + 1])
        return dp[d][0] if dp[d][0] < float('inf') else -1
