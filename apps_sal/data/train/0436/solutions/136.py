import sys
sys.setrecursionlimit(1500000)


class Solution:

    def minDays(self, n: int) -> int:

        @lru_cache(None)
        def go(x):
            if x == 0:
                return 0
            best = 1e+100
            if x % 2 == 0:
                best = min(best, go(x // 2) + 1)
            if x % 3 == 0:
                best = min(best, go(x // 3) + 1)
            if x <= 1024 or (x % 2 > 0 or x % 3 > 0):
                best = min(best, go(x - 1) + 1)
            return best
        return go(n)
