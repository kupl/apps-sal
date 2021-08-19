from functools import lru_cache


class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(None)
        def dfs(i, r, t):
            if i == 0:
                return 1
            s = 0
            for k in range(6):
                if r == k:
                    if t < rollMax[k]:
                        s += dfs(i - 1, r, t + 1)
                else:
                    s += dfs(i - 1, k, 1)
            return s
        return dfs(n, -1, 0) % (10 ** 9 + 7)
