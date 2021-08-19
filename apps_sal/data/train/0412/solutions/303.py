class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        @lru_cache(maxsize=None)
        def nrolls(d, t):
            if d == 0:
                if t == 0:
                    return 1
                else:
                    return 0
            if d > t or t < 0:
                return 0
            res = 0
            for i in range(1, f + 1):
                res += nrolls(d - 1, t - i)
            return res % (10 ** 9 + 7)
        return nrolls(d, target)
