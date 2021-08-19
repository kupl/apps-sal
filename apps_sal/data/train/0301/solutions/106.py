class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)

        @lru_cache(None)
        def fun(i, j):
            if i == n or j == m:
                return 0
            loc = -1
            for k in range(j, m):
                if B[k] == A[i]:
                    loc = k
                    break
            if loc == -1:
                return fun(i + 1, j)
            else:
                return max(fun(i + 1, j), 1 + fun(i + 1, loc + 1))
        return fun(0, 0)
