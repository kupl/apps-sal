import sys
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from collections import deque
from bisect import bisect_left
from itertools import product


def I():
    return int(sys.stdin.readline())


def MI():
    return list(map(int, sys.stdin.readline().split()))


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LI2(N):
    return [list(map(int, sys.stdin.readline().split())) for i in range(N)]


def LSI():
    return list(map(int, list(sys.stdin.readline().rstrip())))


def LSI2(N):
    return [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(N)]


def ST():
    return sys.stdin.readline().rstrip()


def LST():
    return sys.stdin.readline().rstrip().split()


def LST2(N):
    return [sys.stdin.readline().rstrip().split() for i in range(N)]


def FILL(i, h):
    return [i for j in range(h)]


def FILL2(i, h, w):
    return [FILL(i, w) for j in range(h)]


def FILL3(i, h, w, d):
    return [FILL2(i, w, d) for j in range(h)]


def FILL4(i, h, w, d, d2):
    return [FILL3(i, w, d, d2) for j in range(h)]


def sisha(num, digit):
    return Decimal(str(num)).quantize(Decimal(digit), rounding=ROUND_HALF_UP)


MOD = 1000000007
INF = float('inf')
sys.setrecursionlimit(10 ** 6 + 10)


def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = MOD
N = 5 * 10 ** 5
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
for i in range(2, N + 1):
    g1.append(g1[-1] * i % mod)
    inverse.append(-inverse[mod % i] * (mod // i) % mod)
    g2.append(g2[-1] * inverse[-1] % mod)
(N, K) = MI()
ans = cmb(2 * N - 1, N - 1, MOD)
if K < N - 1:
    for i in range(K + 1, N):
        ans -= cmb(N, i, MOD) * cmb(N - 1, i, MOD)
print(ans % MOD)
