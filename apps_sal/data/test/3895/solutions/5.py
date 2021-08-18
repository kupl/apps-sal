import sys
from collections import defaultdict


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def solve():
    n = int(input())
    f = [int(i) for i in input().split()]
    inv = defaultdict(set)

    for i, y in enumerate(f, start=1):
        inv[y].add(i)

    m = len(inv)
    g = [0] * (n + 1)
    h = [0] * (m + 1)

    for i, x in enumerate(inv, start=1):
        if x not in inv[x]:
            print(-1)
            return

        for a in inv[x]:
            g[a] = i

        h[i] = x

    print(m)
    print(*g[1:])
    print(*h[1:])


def __starting_point():
    solve()


__starting_point()
