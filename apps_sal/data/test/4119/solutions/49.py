import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n, m = inl()
    X = inl()
    X.sort()
    x = X[0]
    D = []
    for i in range(1, m):
        d = X[i] - x
        D.append(d)
        x = X[i]
    D.sort()
    k = max(m - n, 0)
    return sum(D[:k])


print(solve())
