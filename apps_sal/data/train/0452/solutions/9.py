class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0
        for k in range(1, d + 1):
            for i in range(1, n + 1):
                max_diff_right = 0
                for j in range(i - 1, k - 2, -1):
                    max_diff_right = max(max_diff_right, jobDifficulty[j])
                    dp[k][i] = min(dp[k][i], dp[k - 1][j] + max_diff_right)
        return dp[d][n]
