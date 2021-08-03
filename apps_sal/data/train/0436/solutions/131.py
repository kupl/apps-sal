import sys


class Solution:
    def minDays(self, n: int) -> int:
        sys.setrecursionlimit(10**6)
        return self.helperFunction(n, {})

    def helperFunction(self, n, d):
        if(n <= 0):
            return 0
        if(d.get(n) is not None):
            return d[n]
        d[n] = 999999
        if(n % 2 == 0):
            d[n] = min(d[n], 1 + self.helperFunction(n - (n / 2), d))
        if(n % 3 == 0):
            d[n] = min(d[n], 1 + self.helperFunction(n - ((2 * n) / 3), d))
        if(n <= 1024 or (n % 2) > 0 or (n % 3) > 0):
            d[n] = min(d[n], 1 + self.helperFunction(n - 1, d))
        return d[n]
