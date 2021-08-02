import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    s = ins()
    if n % 2 == 1:
        return False
    t = s[: n // 2]
    return s == t + t


print("Yes" if solve() else "No")
