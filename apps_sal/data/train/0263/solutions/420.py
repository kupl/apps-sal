from functools import lru_cache


class Solution:

    def knightDialer(self, n: int) -> int:
        to = {0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9), 5: (), 6: (0, 1, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4)}

        @lru_cache(maxsize=None)
        def dfs(i: int, k: int) -> int:
            if i not in to:
                return 0
            if k == 1:
                return 1
            return sum([dfs(t, k - 1) for t in to[i]])
        return sum([dfs(i, n) for i in range(10)]) % (10 ** 9 + 7)
