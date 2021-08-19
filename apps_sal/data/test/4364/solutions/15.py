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
    a = int(S[:2])
    b = int(S[2:])
    am = 0 < a < 13
    bm = 0 < b < 13
    if am and bm:
        return 'AMBIGUOUS'
    elif am:
        return 'MMYY'
    elif bm:
        return 'YYMM'
    else:
        return 'NA'


print(solve())
