import sys

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def solve():
    n, l, r = map(int, input().split())
    ans = f(n, r) - f(n, l - 1)

    print(ans)

def f(n, i):
    if n == 0:
        return 0
    if i == 0:
        return 0

    mx = 2**(n.bit_length())

    if i == mx//2:
        return n//2 + n%2
    elif i < mx//2:
        return f(n//2, i)
    else:
        return n//2 + n%2 + f(n//2, i - mx//2)

def __starting_point():
    solve()
__starting_point()
