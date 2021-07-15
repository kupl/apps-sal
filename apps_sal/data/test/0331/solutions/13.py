import sys

def solve():
    n, m, k = map(int, input().split())
    m = m - 1
    a = [int(i) for i in input().split()]

    min_d = 10**9

    for i in range(n):
        if 0 < a[i] <= k:
            min_d = min(min_d, abs((m - i)) * 10)

    ans = min_d
    print(ans)

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def __starting_point():
    solve()
__starting_point()
