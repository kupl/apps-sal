import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def is_pal(s):
    return s[::-1] == s


def solve():
    S = ins()
    n = len(S)
    return is_pal(S) and is_pal(S[: n // 2]) and is_pal(S[n // 2 + 1:])


print("Yes" if solve() else "No")
