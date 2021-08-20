import sys
from collections import Counter
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
    c = Counter()
    for x in a:
        c[x] += 1
    ans = 0
    for (k, v) in c.items():
        if k <= v:
            ans += v - k
        else:
            ans += v
    return ans


print(solve())
