from functools import lru_cache


class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        (R, C) = (len(A), len(A[0]))

        def col_lower(j1, j2):
            return all((A[i][j1] <= A[i][j2] for i in range(R)))

        @lru_cache(None)
        def LIS(i):
            if i == 0:
                return 1
            return max((LIS(j) for j in range(i) if col_lower(j, i)), default=0) + 1
        return C - max((LIS(i) for i in range(C)))
