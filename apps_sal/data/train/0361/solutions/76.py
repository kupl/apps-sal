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
                left = dfs(i, y)
                right = dfs(x - i, y)
                result = min(result, left + right)

            for k in range(1, (y // 2) + 1):
                bottom = dfs(x, k)
                top = dfs(x, y - k)
                result = min(result, bottom + top)

            for size in range(1, min(x, y)):
                for i in range(1, x - size):
                    for k in range(1, y - size):
                        partition1 = dfs(i + size, k)
                        partition2 = dfs(x - size - i, k + size)
                        partition3 = dfs(x - i, y - size - k)
                        partition4 = dfs(i, y - k)
                        partition5 = 1

                        curr_result = partition1 + partition2 + partition3 + partition4 + partition5
                        result = min(result, curr_result)

            return result

        return dfs(n, m)
