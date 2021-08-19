class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if N < d:
            return -1
        dp = [[float('inf')] * (N + 1) for _ in range(d + 1)]
        dp[0][0] = 0
        for i in range(1, d + 1):
            for j in range(i, N + 1):
                for k in range(i - 1, j):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + max(jobDifficulty[k:j]))
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
