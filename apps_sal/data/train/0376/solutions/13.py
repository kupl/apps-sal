class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0 for i in range(n)]for j in range(n)]
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = math.inf
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (A[i] * A[k] * A[j]))
        return sum(A) if dp[0][n - 1] == math.inf else dp[0][n - 1]
