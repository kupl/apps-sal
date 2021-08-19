import sys
from math import *
from collections import deque


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    (n, k, x) = mints()
    a = list(mints())
    d = [-1e+50] * n
    p = [-1e+50] * n
    for i in range(0, k):
        d[i] = a[i]
    q = deque()
    for xx in range(1, x):
        (d, p) = (p, d)
        q.clear()
        for nn in range(xx - 1, n):
            while len(q) != 0 and q[0][1] < nn - k:
                q.popleft()
            if len(q):
                d[nn] = q[0][0] + a[nn]
            else:
                d[nn] = -1e+50
            while len(q) and q[-1][0] <= p[nn]:
                q.pop()
            q.append((p[nn], nn))
    m = -1
    for i in range(n - k, n):
        m = max(m, d[i])
    print(m)


solve()
