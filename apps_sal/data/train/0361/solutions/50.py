from functools import lru_cache


class Solution:

    @lru_cache(None)
    def tilingRectangle(self, n: int, m: int) -> int:
        (n, m) = (min(n, m), max(n, m))
        if m == n:
            return 1
        if m % n == 0:
            return m // n
        s1 = m * n
        for x in range(1, m // 2 + 1):
            s1 = min(s1, self.tilingRectangle(n, x) + self.tilingRectangle(n, m - x))
        for y in range(1, n // 2 + 1):
            s1 = min(s1, self.tilingRectangle(y, m) + self.tilingRectangle(n - y, m))
        s2 = m * n
        for xL in range(1, m // 2 + 1):
            for xR in range(1, m - xL):
                for yL in range(1, n // 2 + 1):
                    for yR in range(1, n - yL):
                        s2 = min(s2, self.tilingRectangle(n - yR, xL) + self.tilingRectangle(yL, m - xL) + self.tilingRectangle(n - yL, xR) + self.tilingRectangle(yR, m - xR) + self.tilingRectangle(n - yL - yR, m - xL - xR))
        return min(s1, s2)
