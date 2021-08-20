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
    (n, k) = inl()
    v = []
    for i in range(n):
        (a, b) = inl()
        v.append((a, b))
    v.sort(reverse=True)
    c = k - 1
    while v:
        (a, b) = v.pop()
        if b > c:
            return a
        c -= b


print(solve())
