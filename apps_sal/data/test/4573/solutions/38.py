import sys
sys.setrecursionlimit(10 ** 8)


def ini():
    return int(sys.stdin.readline())


def inl():
    return [int(x) for x in sys.stdin.readline().split()]


def ins():
    return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print('\x1b[33m', *a, '\x1b[0m', **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    x = inl()
    y = sorted(x)
    p = y[n // 2 - 1]
    q = y[n // 2]
    for i in range(n):
        if x[i] < q:
            print(q)
        else:
            print(p)


solve()
