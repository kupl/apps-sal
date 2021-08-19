from collections import defaultdict


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        m = defaultdict(int)

        def do(n):
            if n == 1:
                return 0
            if m[n] != 0:
                return m[n]
            elif n % 2 == 0:
                m[n] = 1 + do(n / 2)
            else:
                m[n] = 1 + do(3 * n + 1)
            return m[n]
        res = []
        for i in range(lo, hi + 1):
            res.append([do(i), i])
        res.sort()
        return res[k - 1][1]
