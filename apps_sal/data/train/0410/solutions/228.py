from functools import lru_cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        @lru_cache
        def getPower(x: int) -> int:
            if x == 1:
                return 1
            if x % 2 == 0:
                return getPower(x // 2) + 1

            if x % 2 == 1:
                return getPower(3 * x + 1) + 1

        powers = [0] * (hi - lo + 1)
        if len(powers) == 1:
            return lo
        for i in range(len(powers)):

            if i + lo != 1:
                powers[i] = getPower(i + lo) - 1
            else:
                powers[i] = getPower(i + lo)

        idxs = sorted(range(len(powers)), key=lambda x: powers[x])
        # print(powers, idxs)
        return lo + idxs[k - 1]
