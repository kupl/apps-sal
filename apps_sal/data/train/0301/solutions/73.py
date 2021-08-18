class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)

        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0:
                return 0
            if A[i] == B[j]:
                return dp(i - 1, j - 1) + 1
            return max(dp(i - 1, j), dp(i, j - 1))
        return dp(n - 1, m - 1)
