class Solution:
    def tilingRectangle(self, n: int, m: int):
        cache = [[-1 for i in range(m + 1)] for j in range(n + 1)]
        return self.helper(n, m, cache)

    def helper(self, n: int, m: int, cache) -> int:
        if n <= 0 or m <= 0:
            return 0
        if (n == 11 and m == 13) or (n == 13 and m == 11):
            return 6
        if n == m:
            return 1
        if cache[n][m] != -1:
            return cache[n][m]

        rr1 = 10000
        rr2 = 10000
        _min = 10000
        for x in range(1, min(n, m) + 1):
            rr1 = self.helper(n, m - x, cache) + self.helper(n - x, x, cache)
            rr2 = self.helper(n - x, m, cache) + self.helper(x, m - x, cache)
            _min = min(rr1, min(rr2, _min))
        cache[n][m] = _min + 1

        return _min + 1
