import sys
from collections import Counter

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    a = inl()
    c = Counter()
    for x in a:
        c[x] += 1
    ans = 0
    for k, v in c.items():
        if k <= v:
            ans += v - k
        else:
            ans += v

    return ans


print(solve())

