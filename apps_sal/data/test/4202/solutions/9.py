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
    (l, r) = inl()
    if r - l > 2200:
        return 0
    a = 2018
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            x = i * j % 2019
            a = min(a, x)
    return a


print(solve())
