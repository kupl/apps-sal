import sys
sys.setrecursionlimit(10 ** 8)


def ini():
    return int(sys.stdin.readline())


def inl():
    return [int(x) for x in sys.stdin.readline().split()]


def ins():
    return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print('\x1b[33m', *a, '\x1b[0m', **dict(file=sys.stderr, **kw))
d = {'SAT': 1, 'FRI': 2, 'THU': 3, 'WED': 4, 'TUE': 5, 'MON': 6, 'SUN': 7}


def solve():
    S = ins()
    return d[S]


print(solve())
