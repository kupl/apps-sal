class Solution:

    def minDeletionSize(self, A: List[str]) -> int:

        @lru_cache(None)
        def dp(i, j):
            if i == n:
                return 0
            a = 1 + dp(i + 1, j)
            b = 10 ** 9
            if j == -1 or all((A[k][i] >= A[k][j] for k in range(m))):
                b = dp(i + 1, i)
            return min(a, b)
        (m, n) = (len(A), len(A[0]))
        return dp(0, -1)
