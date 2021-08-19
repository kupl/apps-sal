class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)

        @lru_cache(None)
        def fun(i, j):
            if i == n or j == m:
                return 0
            if A[i] == B[j]:
                return 1 + fun(i + 1, j + 1)
            else:
                return max(fun(i + 1, j), fun(i, j + 1))
        return fun(0, 0)
