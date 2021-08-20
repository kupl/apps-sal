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
    (x, y) = inl()
    if x > y:
        (x, y) = (y, x)
    d = y - x
    if d <= 1:
        return False
    return True


print('Alice' if solve() else 'Brown')
