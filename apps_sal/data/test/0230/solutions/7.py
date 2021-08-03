import random
from collections import defaultdict


class RollingHash():

    def __init__(self, S, b=3491, m=999999937):
        """任意の基数と法でハッシュを生成する"""
        n = len(S)
        self.prefix = prefix = [0] * (n + 1)
        self.power = power = [1] * (n + 1)
        self.b = b
        self.m = m
        for i in range(n):
            c = ord(S[i])
            prefix[i + 1] = (prefix[i] * b + c) % m
            power[i + 1] = (power[i] * b) % m

    def get(self, l, r):
        """S[l, r) のハッシュを求める"""
        return (self.prefix[r] - self.power[r - l] * self.prefix[l]) % self.m

    def concat(self, h1, h2, l2):
        """S1+S2 のハッシュを、それぞれのハッシュから求める"""
        return (self.power[l2] * h1 + h2) % self.m

    def lcp(self, l1, r1, l2, r2):
        """S[l1, r1) とS[l2, r2) の最大共通接頭辞を求める"""
        low = 0
        high = min(r1 - l1, r2 - l2) + 1
        while high - low > 1:
            mid = (high + low) // 2
            if self.get(l1, l1 + mid) == self.get(l2, l2 + mid):
                low = mid
            else:
                high = mid
        return low


def read():
    N = int(input().strip())
    S = input().strip()
    return N, S


def solve(N, S):
    ans = []
    for m in [999999937, 10**9 + 7]:
        b = random.randint(10000, m - 1)
        rh = RollingHash(S, b=b, m=m)
        low = 0
        high = (N + 1) // 2 + 1
        dmax = defaultdict(int)
        dmin = defaultdict(int)
        while high - low > 1:
            dmax.clear()
            dmin.clear()
            mid = (high + low) // 2
            for i in range(0, N - mid + 1):
                h = rh.get(i, i + mid)
                dmax[h] = max(dmax[h], i + 1)
                dmin[h] = max(dmin[h], N + 1 - i)
            is_match = False
            for h in dmax.keys():
                if dmax[h] - (N + 2 - dmin[h]) >= mid:
                    is_match = True
                    break
            if is_match:
                low = mid
            else:
                high = mid
        ans.append(low)
    return min(ans)


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))


__starting_point()
