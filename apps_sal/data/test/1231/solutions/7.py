import sys

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def solve():
    a, b = map(int, input().split())

    if (a + b) > 0 and abs(a - b) <= 1:
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)

def __starting_point():
    solve()
__starting_point()
