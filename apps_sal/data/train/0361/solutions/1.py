from functools import lru_cache


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x == y:
                return 1
            if x == 1:
                return y
            if y == 1:
                return x

            result = x * y

            for i in range(1, (x // 2) + 1):
                result = min(result, dfs(i, y) + dfs(x - i, y))

            for k in range(1, (y // 2) + 1):
                result = min(result, dfs(x, k) + dfs(x, y - k))

            for centre_sq_size in range(1, min(x, y)):
                for i in range(1, x - centre_sq_size):
                    for k in range(1, y - centre_sq_size):
                        partition1 = dfs(i + centre_sq_size, k)
                        partition2 = dfs(x - i - centre_sq_size, k + centre_sq_size)
                        partition3 = dfs(i, y - k)
                        partition4 = dfs(x - i, y - k - centre_sq_size)
                        partition5 = 1

                        result = min(result, partition1 + partition2 + partition3 + partition4 + partition5)

            return result

        return dfs(n, m)
