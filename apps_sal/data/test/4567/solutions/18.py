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
    s = [ini() for _ in range(n)]
    a = sum(s)
    if a % 10 != 0:
        return a
    m = 1000
    for x in s:
        if x % 10 != 0 and m > x:
            m = x
    if m == 1000:
        return 0
    return a - m


print(solve())
