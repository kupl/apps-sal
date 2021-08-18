from functools import lru_cache


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:

        @lru_cache(None)
        def dp(i, j):
            return min([dp(i, k) + dp(k, j) + A[i] * A[k] * A[j] for k in range(i + 1, j)] or [0])
        return dp(0, len(A) - 1)
