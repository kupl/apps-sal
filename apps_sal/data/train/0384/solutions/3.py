from bisect import bisect_left, bisect_right


class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        n = len(A)
        ret = 0

        A.sort()
        ret = 0
        f = {}

        for i, x in enumerate(A):
            if x not in f:
                f[x] = [i, i]
            else:
                f[x][1] = i

        ret = 0

        for x in f:
            l, r = f[x]
            sl = l
            sr = n - r - 1
            se = r - l + 1
            ret += (2**sl - 1) * (2**se - 1) * x
            ret -= (2**sr - 1) * (2**se - 1) * x

        return ret % (10 ** 9 + 7)
