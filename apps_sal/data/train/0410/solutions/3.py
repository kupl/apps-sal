from functools import lru_cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        res = []
        for i in range(lo, hi + 1):
            res.append((self.power(i), i))
        res.sort()
        return res[k - 1][1]

    @lru_cache
    def power(self, num):
        if num == 1:
            return 0
        if num % 2 == 0:
            return 1 + self.power(num // 2)
        else:
            return 1 + self.power(3 * num + 1)
