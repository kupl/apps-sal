from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def I():
    return int(sys.stdin.readline())


def LS():
    return [list(x) for x in sys.stdin.readline().split()]


def S():
    res = list(sys.stdin.readline())
    if res[-1] == '\n':
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


sys.setrecursionlimit(1000000)
mod = 1000000007


def solve():
    (n, m) = LI()
    f = [1]
    N = 10 ** 6
    for i in range(1, N + 1):
        f.append(f[-1] * i % mod)
    inv = [None] * (N + 1)
    inv[N] = pow(f[N], mod - 2, mod)
    for i in range(N)[::-1]:
        inv[i] = inv[i + 1] * (i + 1) % mod
    print(f[2 * m + n - 1] * inv[n - 1] * inv[2 * m] % mod)
    return


def __starting_point():
    solve()


__starting_point()
