class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[float('inf')]*n for _ in range(n)]
        for l in range(2, n):
            for i in range(n-l):
                j = i + l                
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], (dp[i][k] if k >= i + 2 else 0) + A[i]*A[k]*A[j]  + (dp[k][j] if j >= k + 2 else 0))
        return dp[0][n-1]
