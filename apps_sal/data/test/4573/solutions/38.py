import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    x = inl()
    y = sorted(x)

    p = y[n // 2 - 1]
    q = y[n // 2]

    for i in range(n):
        if x[i] < q:
            print(q)
        else:
            print(p)


solve()

