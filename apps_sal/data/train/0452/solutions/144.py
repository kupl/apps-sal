class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        dp = [[float('inf') for col in range(d + 1)] for row in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, 1 + n):
            for k in range(1, 1 + d):
                for j in range(i, k - 1, -1):
                    dp[i][k] = min(dp[i][k], dp[j - 1][k - 1] + max(jobDifficulty[j - 1:i]))
        return dp[-1][-1]
