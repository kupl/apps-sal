from functools import lru_cache


class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(maxsize=None)
        def dfs(left, last, length):
            if left == 0:
                if length <= rollMax[last]:
                    return 1
                else:
                    return 0
            total = 0
            for i in range(6):
                if i == last:
                    if length + 1 <= rollMax[last]:
                        total += dfs(left - 1, i, length + 1)
                else:
                    total += dfs(left - 1, i, 1)
            return total
        return dfs(n, -1, 0) % (10 ** 9 + 7)
