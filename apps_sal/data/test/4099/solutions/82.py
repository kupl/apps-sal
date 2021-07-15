import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n, k, m = inl()
    a = inl()
    s = sum(a)
    y = m * n - s
    if y > k:
        return -1
    return max(y, 0)


print(solve())

