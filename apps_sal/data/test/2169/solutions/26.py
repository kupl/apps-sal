import bisect
import math
from collections import defaultdict
import sys
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
printout = sys.stdout.write
sprint = sys.stdout.flush
sys.setrecursionlimit(10 ** 7)
INF = 1 << 50
EPS = 1e-08
mod = 998244353


def intread():
    return int(sysread())


def mapline(t=int):
    return list(map(t, sysread().split()))


def mapread(t=int):
    return list(map(t, read().split()))


def run():
    (H, W, D) = mapline()
    A = [[-1] * (W + 1) for _ in range(H + 1)]
    for i in range(1, H + 1):
        A[i][1:] = mapline()
    V = [-1] * (H * W + 1)
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            V[A[i][j]] = (i, j)
    cache = [-1] * (H * W + 1)
    Q = intread()
    for _ in range(Q):
        (l, r) = mapline()
        if cache[r] == -1:
            mostR = r + (H * W - r) // D * D
            mostL = l % D
            if not mostL:
                mostL = D
            (ci, cj) = V[mostR]
            tmp = 0
            cache[mostR] = 0
            for v in range(mostR - D, mostL - D, -D):
                (ni, nj) = V[v]
                tmp += abs(ni - ci) + abs(nj - cj)
                cache[v] = tmp
                (ci, cj) = (ni, nj)
        print(cache[l] - cache[r])


def __starting_point():
    run()


__starting_point()
