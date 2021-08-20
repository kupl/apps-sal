class Solution:

    def minScoreTriangulation(self, a: List[int]) -> int:
        n = len(a)
        dp = [[float('inf')] * n for _ in range(n)]
        for l in range(2, n):
            for i in range(n - l):
                j = i + l
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], (dp[i][k] if k >= i + 2 else 0) + a[i] * a[k] * a[j] + (dp[k][j] if j >= k + 2 else 0))
        return dp[0][n - 1]
