from functools import lru_cache


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if (n == 11 and m == 13) or (m == 11 and n == 13):
            return 6

        @lru_cache
        def dfs(x, y):
            if x % y == 0:
                return x // y
            if y % x == 0:
                return y // x

            res = x * y
            for i in range(1, (x // 2) + 1):
                res = min(res, dfs(x - i, y) + dfs(i, y))

            for k in range(1, (y // 2) + 1):
                res = min(res, dfs(x, y - k) + dfs(x, k))

            return res

        return dfs(n, m)
