import sys
from bisect import bisect


def input():
    return sys.stdin.readline().strip()


def solve():
    n, q = list(map(int, input().split()))
    was = set()
    Q = [None] * q
    all = [0] * (2 * q)
    for i in range(q):
        x, y, t = input().split()
        x, y = int(x), int(y)
        Q[i] = (x, y, t)
        all[2 * i] = x
        all[2 * i + 1] = y
    all.sort()
    i = 0
    p = -1
    F = dict()
    for j in range(2 * q):
        v = all[j]
        if v != p:
            all[i] = v
            F[v] = i
            i += 1
        p = v
    sz = i
    all = all[:sz]
    V = [0] * (2 * sz)
    H = [0] * (2 * sz)
    for x, y, t in Q:
        if (x, y) in was:
            print(0)
        else:
            was.add((x, y))
            if t == 'L':
                TA = H
                TB = V
            else:
                x, y = y, x
                TA = V
                TB = H
            v = F[y] + sz
            r = 0
            while v > 0:
                r = max(r, TA[v])
                v //= 2
            c = x - r
            print(c)
            r = F[x] + sz
            l = bisect(all, x - c) + sz
            while l <= r:
                if l % 2 == 1:
                    TB[l] = max(TB[l], y)
                if r % 2 == 0:
                    TB[r] = max(TB[r], y)
                l = (l + 1) // 2
                r = (r - 1) // 2


solve()
