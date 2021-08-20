class Solution:

    def minDays(self, n: int) -> int:

        def fun(n, d):
            if n <= 1:
                return n
            if n in d:
                return d[n]
            d[n] = min(n % 2 + fun(n // 2, d), n % 3 + fun(n // 3, d)) + 1
            return d[n]
        d = {}
        return fun(n, d)
