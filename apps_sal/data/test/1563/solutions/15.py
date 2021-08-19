from sys import stdin
from collections import *


def arr_inp(n):
    if n == 1:
        return [int(x) for x in stdin.readline().split()]
    elif n == 2:
        return [float(x) for x in stdin.readline().split()]
    else:
        return list(stdin.readline()[:-1])


def main():
    (n, m) = arr_inp(1)
    (c, ans, ma) = (arr_inp(1), float('inf'), 0)
    mem = defaultdict(set)
    for i in range(m):
        (u, v) = arr_inp(1)
        u -= 1
        v -= 1
        if c[u] != c[v]:
            mem[c[u]].add(c[v])
            mem[c[v]].add(c[u])
    for (i, j) in list(mem.items()):
        if len(j) > ma:
            ma = max(ma, len(j))
            ans = i
        if len(j) == ma:
            ans = min(ans, i)
    print(ans if ans != float('inf') else min(c))


def __starting_point():
    main()


__starting_point()
