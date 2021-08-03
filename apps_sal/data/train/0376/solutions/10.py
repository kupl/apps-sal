class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        N = len(A)
        dp = [
            [0 for j in range(N)] for i in range(N)
        ]

        for l in range(3, N + 1):
            for i in range(N - l + 1):
                j = i + l - 1
                for k in range(i + 1, j):
                    val = dp[i][k] + dp[k][j] + A[i] * A[k] * A[j]
                    if not dp[i][j] or dp[i][j] > val:
                        dp[i][j] = val
        return dp[0][N - 1]
