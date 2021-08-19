from functools import lru_cache


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        @lru_cache(None)
        def dp(k: int, n: int) -> int:
            if k <= 0:
                return 0
            if k == 1:
                return n
            # Following line is required; o.w. result is not right.
            if n <= 1:
                return n
            # Find the first floor where dp(k - 1, i - 1) >= dp(k, n - i)
            # such point must exist because dp(k, n-i) has min as dp(k, 0) == 0
            left, right = 1, n
            while left <= right:
                mid = (left + right) // 2
                if dp(k - 1, mid - 1) >= dp(k, n - mid):
                    right = mid - 1
                else:
                    left = mid + 1
            return 1 + dp(k - 1, left - 1)

        return dp(K, N)
