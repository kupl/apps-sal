import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n, k = inl()
    v = []
    for i in range(n):
        a, b = inl()
        v.append((a, b))
    v.sort(reverse=True)
    c = k - 1
    while v:
        a, b = v.pop()
        if b > c:
            return a
        c -= b


print(solve())

