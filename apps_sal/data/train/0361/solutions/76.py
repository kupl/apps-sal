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

            # Max possible result full of squares of side 1
            result = x * y

            # Splitting x into two parts
            for i in range(1, (x // 2) + 1):
                left = dfs(i, y)
                right = dfs(x - i, y)
                result = min(result, left + right)

            # Splitting y into two parts
            for k in range(1, (y // 2) + 1):
                bottom = dfs(x, k)
                top = dfs(x, y - k)
                result = min(result, bottom + top)

            # A central square with 4 other rectangles bounding it
            for size in range(1, min(x, y)):
                for i in range(1, x - size):
                    for k in range(1, y - size):
                        partition1 = dfs(i + size, k)
                        partition2 = dfs(x - size - i, k + size)
                        partition3 = dfs(x - i, y - size - k)
                        partition4 = dfs(i, y - k)
                        partition5 = 1  # A square of side 'size'. dfs(size, size) = 1

                        curr_result = partition1 + partition2 + partition3 + partition4 + partition5
                        result = min(result, curr_result)

            return result

        return dfs(n, m)
