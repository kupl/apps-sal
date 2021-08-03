class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def ok(n, x):
            if n == 0:
                return True
            elif x == 0:
                return False
            else:
                if n % 2 == 0 and ok(n // 2, x - 1):
                    return True
                if n % 3 == 0 and ok(n - 2 * n // 3, x - 1):
                    return True
                return ok(n - 1, x - 1)

        left = 0
        right = n + 1
        while right - left > 1:
            mid = (left + right) // 2
            if ok(n, mid):
                right = mid
            else:
                left = mid
        return right
