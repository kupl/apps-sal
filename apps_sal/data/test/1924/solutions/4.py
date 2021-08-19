"""
研究室PCでの解答
解説AC
"""
import math
import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10 ** 7)
mod = 10 ** 9 + 7


def main():
    (r1, c1, r2, c2) = list(map(int, ipt().split()))
    N = r2 + c2 + 2
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]

    def cmb(n, r, mod=10 ** 9 + 7):
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod
    for i in range(2, N + 1):
        g1.append(g1[-1] * i % mod)
        inverse.append(-inverse[mod % i] * (mod // i) % mod)
        g2.append(g2[-1] * inverse[-1] % mod)
    print((cmb(r2 + c2 + 2, r2 + 1) + cmb(r1 + c1, r1) - cmb(r2 + c1 + 1, r2 + 1) - cmb(r1 + c2 + 1, r1)) % mod)
    return None


def __starting_point():
    main()


__starting_point()
