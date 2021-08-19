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
    return


def B():
    return


def C():

    def bfs(s, g, n):
        bfs_map = [-1 for i in range(n)]
        bfs_map[s] = 0
        q = deque()
        q.append(s)
        fin = False
        while q:
            x = q.popleft()
            for y in range(n):
                if c[x][y] > 0 and bfs_map[y] < 0:
                    bfs_map[y] = bfs_map[x] + 1
                    if y == g:
                        fin = True
                        break
                    q.append(y)
            if fin:
                break
        if bfs_map[g] == -1:
            return [None, 0]
        path = [None for i in range(bfs_map[g] + 1)]
        m = float('inf')
        path[bfs_map[g]] = g
        y = g
        for i in range(bfs_map[g])[::-1]:
            for x in range(n + 1):
                if c[x][y] > 0 and bfs_map[x] == bfs_map[y] - 1:
                    path[i] = x
                    if c[x][y] < m:
                        m = c[x][y]
                    y = x
                    break
        return [path, m]

    def ford_fulkerson(s, g, c, n):
        while 1:
            (p, m) = bfs(s, g, n)
            if not m:
                break
            for i in range(len(p) - 1):
                c[p[i]][p[i + 1]] -= m
                c[p[i + 1]][p[i]] += m
        return sum(c[g])
    n = I()
    a = LI()
    e = n + 2
    ma = 10 ** 9
    c = [[0] * e for i in range(e)]
    for i in range(n):
        d = i + 1
        j = 2 * d
        c[0][d] = ma
        c[d][n + 1] = ma - a[i]
        while j <= n:
            c[j][d] = float('inf')
            j += d
    print(ma * n - ford_fulkerson(0, n + 1, c, e))
    return


def D():
    return


def E():
    return


def F():
    return


def __starting_point():
    C()


__starting_point()
