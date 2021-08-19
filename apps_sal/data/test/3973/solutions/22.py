from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random


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


def A():
    n = I()
    return


def B():
    n = I()
    return


def C():
    (n, m) = LI()
    a = LI()
    for i in range(n):
        a[i] -= 1
    b = [0] * (m + 10)
    ans = 0
    f = [0] * (m + 10)
    for i in range(n - 1):
        r = (a[i + 1] - a[i]) % m
        ans += r
        if r < 2:
            continue
        if a[i + 1] >= (a[i] + 2) % m:
            f[(a[i] + 2) % m] += 1
            b[(a[i] + 2) % m] += 1
            b[a[i + 1] + 1] -= 1
            f[a[i + 1] + 1] -= r
        else:
            b[0] += 1
            f[0] += (-a[i] - 1) % m
            b[a[i + 1] + 1] -= 1
            f[a[i + 1] + 1] -= r
            b[a[i] + 2] += 1
            f[a[i] + 2] += 1
            b[m] -= 1
    for i in range(m - 1):
        b[i + 1] += b[i]
    for i in range(m - 1):
        f[i + 1] += f[i] + b[i]
    print(ans - max(f))
    return


def D():
    n = I()
    return


def E():
    n = I()
    return


def F():
    n = I()
    return


def __starting_point():
    C()


__starting_point()
