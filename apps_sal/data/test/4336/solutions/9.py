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
    (w, h, x, y) = inl()
    a = w * h / 2.0
    multi = 1 if 2 * x == w and 2 * y == h else 0
    return (float(a), multi)


print(*solve())
