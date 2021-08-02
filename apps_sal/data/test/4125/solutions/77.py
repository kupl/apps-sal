import sys
import math

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n, start = inl()
    X = inl()
    g = None
    for x in X:
        d = abs(x - start)
        if g is None:
            g = d
        else:
            g = math.gcd(g, d)
    return g


print(solve())
