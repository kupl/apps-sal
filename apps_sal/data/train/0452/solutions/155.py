class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        difficulties = [[0] * n for _ in range(n)]
        for i in range(n):
            difficulties[i][i] = jobDifficulty[i]
            for j in range(i + 1, n):
                difficulties[i][j] = max(difficulties[i][j - 1], jobDifficulty[j])
        dp = [[float('inf')] * (d + 1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = difficulties[0][i]
            for p in range(2, d + 1):
                for j in range(i):
                    dp[i][p] = min(dp[i][p], dp[j][p - 1] + difficulties[j + 1][i])
        return dp[n - 1][d]
