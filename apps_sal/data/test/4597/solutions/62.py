import sys
sys.setrecursionlimit(10 ** 8)


def ini():
    return int(sys.stdin.readline())


def inl():
    return [int(x) for x in sys.stdin.readline().split()]


def ins():
    return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print('\x1b[33m', *a, '\x1b[0m', **dict(file=sys.stderr, **kw))
MOD = 10 ** 9 + 7


def solve():
    n = ini()
    p = 1
    for i in range(1, n + 1):
        p *= i
        p %= MOD
    return p


print(solve())
