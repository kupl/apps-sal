from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return [list(x) for x in sys.stdin.readline().split()]


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
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


sys.setrecursionlimit(10000000)
mod = 1000000007


def solve():
    n = I()
    a = []
    b = []
    c = []
    for _ in range(n):
        x, y, z = LI()
        a.append(x)
        b.append(y)
        c.append(z)
    v = [[] for i in range(n)]
    for _ in range(n - 1):
        x, y = LI()
        x -= 1
        y -= 1
        v[x].append(y)
        v[y].append(x)
    if b.count(1) != c.count(1):
        print(-1)
        return
    q = deque([0])
    q2 = deque()
    d = [1] * n
    d[0] = 0
    ans = 0
    p = [[0] * 2 for i in range(n)]
    while q:
        x = q.popleft()
        ax = a[x]
        if b[x] != c[x]:
            p[x][b[x]] = 1
        for y in v[x]:
            if d[y]:
                d[y] = 0
                if ax < a[y]:
                    a[y] = ax
                q.append(y)
                q2.append((x, y))
    while q2:
        x, y = q2.pop()
        p[x][0] += p[y][0]
        p[x][1] += p[y][1]
        m = min(p[x])
        ans += m * a[x]
        p[x][0] -= m
        p[x][1] -= m
    print(ans * 2)
    return


def __starting_point():
    solve()


__starting_point()
