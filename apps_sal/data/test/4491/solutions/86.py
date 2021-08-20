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
    a1 = inl()
    a2 = inl()
    (b1, b2) = (a1[0], a1[0] + a2[0])
    for i in range(1, n):
        b2 = max(b2 + a2[i], b1 + a1[i] + a2[i])
        b1 = b1 + a1[i]
    return b2


print(solve())
