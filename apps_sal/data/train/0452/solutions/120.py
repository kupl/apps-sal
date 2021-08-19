class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        dp = [[float('inf') for i in range(len(jobDifficulty))] for j in range(d)]
        for i in range(len(jobDifficulty)):
            dp[0][i] = max(jobDifficulty[:i + 1])
        for i in range(1, d):
            for j in range(i, len(jobDifficulty)):
                for k in range(j):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + max(jobDifficulty[k + 1:j + 1]))
        return dp[-1][-1]
