import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def main():
    (n, m) = list(map(int, input().split()))
    to = defaultdict(list)
    ot = defaultdict(list)
    for _ in range(m):
        (s, t) = list(map(int, input().split()))
        (s, t) = (s - 1, t - 1)
        to[s].append(t)
        ot[t].append(s)
    ev = [0] * n
    for u in range(n - 2, -1, -1):
        s = 0
        for ku in to[u]:
            s += ev[ku]
        ev[u] = s / len(to[u]) + 1
    pe = [[0] * n for _ in range(n)]
    pn = [0] * n
    for u in range(n):
        p = 0
        for ou in ot[u]:
            p += pe[ou][u]
        if u == 0:
            p = 1
        pn[u] = p
        sz = len(to[u])
        for ku in to[u]:
            pe[u][ku] = p / sz
    dx = 0
    for u in range(n - 1):
        sz = len(to[u])
        if sz == 1:
            continue
        mx = 0
        for ku in to[u]:
            mx = max(ev[ku], mx)
        nev = ((ev[u] - 1) * sz - mx) / (sz - 1) + 1
        de = pn[u] * (ev[u] - nev)
        dx = max(dx, de)
    print(ev[0] - dx)


main()
