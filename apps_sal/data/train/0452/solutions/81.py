from functools import lru_cache


class Solution:
    def minDifficulty(self, A, d):

        n = len(A)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(n, d):

            if n < d:
                return math.inf
            if d == 1:
                return max(A[:n])
            return min(dp(t, d - 1) + max(A[t: n]) for t in range(n))

        return dp(n, d)
