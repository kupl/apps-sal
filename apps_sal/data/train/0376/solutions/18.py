class Solution:

    def minScoreTriangulation(self, A: List[int]) -> int:
        if len(A) == 3:
            return A[0] * A[1] * A[2]
        n = len(A)
        dp = [[float('inf') for j in range(n)] for i in range(n)]

        def helper(i, j):
            if j - i <= 1:
                return 0
            if dp[i][j] != float('inf'):
                return dp[i][j]
            res = float('inf')
            for k in range(i + 1, j):
                res = min(res, helper(i, k) + A[i] * A[k] * A[j] + helper(k, j))
            dp[i][j] = res
            return dp[i][j]
        return helper(0, n - 1)
