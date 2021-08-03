class Solution:
    def numWays(self, s: str) -> int:
        d = []
        for ind, val in enumerate(s):
            if val == '1':
                d.append(ind)

        n = len(d)
        ndiv = n // 3
        if ndiv * 3 != n:
            return 0

        if n == 0:
            n = len(s)
            res = (n - 1) * (n - 2) >> 1
        else:
            res = (d[ndiv] - d[ndiv - 1]) * (d[2 * ndiv] - d[2 * ndiv - 1])

        return res % (1000000007)
