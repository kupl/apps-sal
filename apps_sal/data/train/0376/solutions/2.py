from functools import lru_cache


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        # If we pick a side of our polygon, it can form n - 2 triangles. Each such triangle forms 2 sub-polygons. We can analyze n - 2 triangles, and get the minimum score for sub-polygons using the recursion.

        # n = len(A)
        # dp = [[0] * n for _ in range(n)]
        # for d in range(2, n):
        #     for i in range(n - d):
        #         j = i + d
        #         dp[i][j] = min(dp[i][k] + dp[k][j] + A[i] * A[j] * A[k] for k in range(i + 1, j))
        # return dp[0][n - 1]

        @lru_cache(None)
        def dp(i, j):
            return min([dp(i, k) + dp(k, j) + A[i] * A[k] * A[j] for k in range(i + 1, j)] or [0])
        return dp(0, len(A) - 1)
