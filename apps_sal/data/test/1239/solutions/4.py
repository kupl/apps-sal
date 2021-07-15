import sys

def solve():
    n = int(input())
    a = sorted([int(i) for i in input().split()])

    cnt = 0
    min_d = 4 * 10**9

    for i in range(n - 1):
        if a[i + 1] - a[i] < min_d:
            cnt = 1
            min_d = a[i + 1] - a[i]
        elif a[i + 1] - a[i] == min_d:
            cnt += 1

    print(min_d, cnt)


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def __starting_point():
    solve()
__starting_point()
