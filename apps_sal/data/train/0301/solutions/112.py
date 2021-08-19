class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        d = {}

        def helper(i, j):
            if i == n or j == m:
                return 0
            if (i, j) in d:
                return d[i, j]
            if A[i] == B[j]:
                d[i, j] = 1 + helper(i + 1, j + 1)
            else:
                d[i, j] = max(helper(i + 1, j), helper(i, j + 1))
            return d[i, j]
        return helper(0, 0)
