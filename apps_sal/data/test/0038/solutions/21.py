import sys


def debug(x, table):
    for (name, val) in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def solve():
    (n, L) = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    for i in range(L):
        B_r = sorted([(b + i) % L for b in B])
        if A == B_r:
            print('YES')
            break
    else:
        print('NO')


def __starting_point():
    solve()


__starting_point()
