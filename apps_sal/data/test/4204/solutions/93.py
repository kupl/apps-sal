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
    S = ins()
    K = ini()
    ones = 0
    for (i, d) in enumerate(S):
        if d != '1':
            break
        ones += 1
    if K <= ones:
        return '1'
    return S[ones]


print(solve())
