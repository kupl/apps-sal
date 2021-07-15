import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    w, h, x, y = inl()
    a = w * h / 2.0
    multi = 1 if (2 * x == w and 2 * y == h) else 0
    return float(a), multi


print(*solve())

