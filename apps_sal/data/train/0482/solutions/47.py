class Solution:

    def mctFromLeafValues(self, A: List[int]) -> int:
        """
        dp(i, j) = dp(i, k) + dp(k, j)
        """

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            min_cost = float('inf')
            for k in range(i, j):
                min_cost = min(min_cost, dp(i, k) + dp(k + 1, j) + max(A[i:k + 1]) * max(A[k + 1:j + 1]))
            return min_cost
        return dp(0, len(A) - 1)
