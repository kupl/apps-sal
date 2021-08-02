import sys
from heapq import heapify, heappushpop


def main():
    rl = sys.stdin.readline
    n = int(rl().strip())
    a = list(map(int, rl().strip().split()))
    b = [-x for x in a]
    b.reverse()
    fl = a[:n]
    fs = sum(fl)
    ll = b[:n]
    ls = sum(ll)
    fdl = [0] * (n + 1)
    ldl = [0] * (n + 1)
    heapify(fl)
    heapify(ll)
    for i in range(1, n + 1):
        fmn = heappushpop(fl, a[n + i - 1])
        lmn = heappushpop(ll, b[n + i - 1])
        fdl[i] = fdl[i - 1] + a[n + i - 1] - fmn
        ldl[i] = ldl[i - 1] + b[n + i - 1] - lmn
    ldl.reverse()
    dif = max([x + y for x, y in zip(fdl, ldl)])
    print((fs + ls + dif))


def __starting_point():
    main()


__starting_point()
