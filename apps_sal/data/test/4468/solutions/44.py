import sys

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n, T = inl()
    t = inl()
    assert len(t) == n
    assert t[0] == 0
    p = 0
    ans = 0
    for i in range(1, n):
        x = t[i]
        ans += min(x - p, T)
        p = x
    ans += T
    return ans


print(solve())
