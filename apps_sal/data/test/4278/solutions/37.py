import sys
from collections import Counter

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    count = Counter()
    for i in range(n):
        s = ins()
        s = "".join(sorted(s))
        count[s] += 1

    ans = 0
    for k, v in count.items():
        if v > 1:
            ans += v * (v - 1) // 2
    return ans


print(solve())
