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
    a = inl()
    a = [0] + a
    a.append(0)
    total = 0
    for i in range(1, n + 2):
        total += abs(a[i] - a[i - 1])
    for i in range(1, n + 1):
        diff = abs(a[i + 1] - a[i - 1]) - abs(a[i] - a[i - 1]) - abs(a[i + 1] - a[i])
        print(total + diff)


solve()
