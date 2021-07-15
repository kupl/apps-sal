class Solution(object):
    def maxSizeSlices(self, A):
        N = len(A)
        A.extend(A)
        NINF = float('-inf')

        @lru_cache(None)
        def dp(i, j, rem):
            if rem == 0:
                return 0
            elif i > j:
                return NINF
            else:
                return max(dp(i+2, j, rem-1) + A[i], dp(i+1, j, rem))

        return max(A[0] + dp(2, N - 2, N // 3 - 1), dp(1, N - 1, N // 3))
