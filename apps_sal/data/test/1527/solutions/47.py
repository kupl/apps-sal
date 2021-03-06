from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
import string
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi


def input():
    return sys.stdin.readline()[:-1]


MOD = int(1000000000.0) + 7
INF = float('inf')


def solve():
    (n, m) = [int(x) for x in input().split()]
    a = []
    starts = []
    for i in range(n):
        a.append(input())
        for j in range(m):
            if a[i][j] == '.':
                starts.append((i, j))

    def bfs(v):
        q = deque([(v, 0)])
        mx = 0
        mv = v
        w = defaultdict(int)
        w[v] = 1
        while q:
            (v, d) = q.popleft()
            if d > mx:
                mv = v
                mx = d
            (i, j) = v
            for (x, y) in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if 0 <= i + x < n and 0 <= j + y < m and (not w[i + x, j + y]) and (a[i + x][j + y] == '.'):
                    w[i + x, j + y] = 1
                    q.append(((i + x, j + y), d + 1))
        return (mx, mv)
    ans = 0
    for start in starts:
        (_, start) = bfs(start)
        (cur, start) = bfs(start)
        ans = max(ans, cur)
    print(ans)


t = 1
for case in range(1, t + 1):
    ans = solve()
'\n1\n4\n-1 1 1 -1\n\n'
