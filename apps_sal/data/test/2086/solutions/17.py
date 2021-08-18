from sys import stdin as si
from collections import Counter as c


class Solution:

    def bazinga(self, n, m, k):
        mnp = sum(m[k[0] - 1:k[1] - 1])
        diff = k[1] - k[0]
        mxp, ans = mnp, 0
        for i in range(1, n):
            mxp += m[(k[0] - i - 1 + n) % n]
            mxp -= m[(k[1] - i - 1 + n) % n]
            if mxp > mnp:
                mnp, ans = mxp, i
        return ans + 1


def __starting_point():
    n = int(si.readline().strip())
    m = list(map(int, si.readline().strip().split()))
    k = tuple(map(int, si.readline().strip().split()))
    S = Solution()
    print(S.bazinga(n, m, k))


'''
http://codeforces.com/contest/939/problem/C
'''
__starting_point()
