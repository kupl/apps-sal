import sys


def solve():
    b1, q, L, m = map(int, input().split())
    a = [int(i) for i in input().split()]

    a = set(a)

    if b1 == 0:
        print(0 if b1 in a else 'inf')
        return

    if q == 1:
        if abs(b1) > L or b1 in a:
            print(0)
        else:
            print('inf')
    elif q == -1:
        if abs(b1) > L or (b1 in a and -b1 in a):
            print(0)
        else:
            print('inf')
    elif q == 0:
        if abs(b1) > L:
            print(0)
        elif 0 in a:
            print(0 if b1 in a else 1)
        else:
            print('inf')
    else:
        b = b1
        ans = 0

        while abs(b) <= L:
            if b not in a:
                ans += 1
            b *= q

        print(ans)


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def __starting_point():
    solve()


__starting_point()
