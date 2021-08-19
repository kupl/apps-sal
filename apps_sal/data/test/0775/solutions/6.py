import sys


def solve():
    (n, m, k) = map(int, sys.stdin.readline().split())
    h = [int(i) - 1 for i in sys.stdin.readline().split()]
    is_hole = [False] * n
    for hi in h:
        is_hole[hi] = True
    pos = 0
    if is_hole[pos]:
        print(pos + 1)
        return
    for i in range(k):
        (u, v) = map(int, sys.stdin.readline().split())
        (u, v) = (u - 1, v - 1)
        if u != pos and v != pos:
            continue
        if u != pos:
            pos = u
        elif v != pos:
            pos = v
        if is_hole[pos]:
            print(pos + 1)
            return
    print(pos + 1)


def debug(x, table):
    for (name, val) in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def __starting_point():
    solve()


__starting_point()
