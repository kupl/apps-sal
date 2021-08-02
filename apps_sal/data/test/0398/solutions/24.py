import sys


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def solve():
    n = int(input())
    A = [int(i) for i in input().split()]

    A.sort()

    for i in range(n - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            print('YES')
            return
    else:
        print('NO')


def __starting_point():
    solve()


__starting_point()
