class Solution:

    def minDays(self, n: int) -> int:
        ONE_LIMIT = 100
        TWO_LIMIT = 30
        f = {1: 1}

        def search(n, one, two):
            if one > ONE_LIMIT:
                return 1000
            if two > TWO_LIMIT:
                return 1000
            if n in f:
                return f[n]
            ans = 1000
            if n % 3 == 0:
                ans = min(ans, search(n // 3, one, two))
            if n % 2 == 0:
                ans = min(ans, search(n // 2, one, two + 1))
            ans = min(ans, search(n - 1, one + 1, two))
            f[n] = 1 + ans
            return f[n]
        search(n, 0, 0)
        return f[n]
