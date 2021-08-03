from functools import lru_cache


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(None)
        def r(v, p, c):
            if c == n:
                return 1
            else:
                t = 0
                for i in range(0, 6):
                    if i == p:
                        if v < rollMax[i]:
                            t += r(v + 1, i, c + 1)
                    else:
                        t += r(1, i, c + 1)

                return t

        return r(0, 0, 0) % (10**9 + 7)
