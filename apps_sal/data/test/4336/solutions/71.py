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
    x = min(x, w - x)
    y = min(y, h - y)
    assert x <= w / 2
    assert y <= h / 2
    a = w * h / 2.0
    multi = 1 if y * w == x * h and (x, y) != (0, 0) else 0
    return (float(a), multi)


print(*solve())
