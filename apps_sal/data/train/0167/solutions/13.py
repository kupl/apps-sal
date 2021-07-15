from functools import lru_cache


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        @lru_cache(None)
        def dp(k: int, n: int) -> int:
            # k == 0 is invalid but not 'impossible'/infinity. Value 0 ensures formula correctness.
            # dp[k][n] = min{1 + max(dp[k-1][i], dp[k][n-i]) for i in [1, n]}
            # dp[0][:]
            if k <= 0:
                return 1 << 31
            if k == 1:
                return n
            if n <= 0:
                return 0
            # Following line is required; o.w. result is not right.
            # When picking 1st floor to drop egg, if it breaks, no more dropping is needed so dp[:][0] == 0
            if n <= 1:
                return n
            # Find the first floor where value starts to increase.
            left, right = 1, n
            while left <= right:
                mid = (left + right) // 2
                if dp(k - 1, mid - 1) >= dp(k, n - mid):
                    right = mid - 1
                else:
                    left = mid + 1
            # Compare points.
            return 1 + dp(k - 1, left - 1)

        return dp(K, N)
