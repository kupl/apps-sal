import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


MOD = 10 ** 9 + 7


def solve():
    n = ini()
    p = 1
    for i in range(1, n + 1):
        p *= i
        p %= MOD
    return p


print(solve())
