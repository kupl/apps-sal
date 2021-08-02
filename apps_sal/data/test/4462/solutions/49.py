import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    a = inl()

    c4, c2 = 0, 0
    for x in a:
        if x % 4 == 0:
            c4 += 1
        elif x % 2 == 0:
            c2 += 1
    c1 = n - c2 - c4

    if c4 == 0:
        return c1 == 0 and c2 >= 2
    return c4 >= c1 or (c4 + 1 == c1 and c2 == 0)


print("Yes" if solve() else "No")
