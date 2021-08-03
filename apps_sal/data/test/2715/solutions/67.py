import sys

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inm(): return map(int, sys.stdin.readline().split())
def inl(): return list(inm())
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

K = ini()
N = 50


def solve():
    a = K // N
    h = (N - 1) + a
    r = K % N
    hs = [h + N - (r - 1)] * r + [h - r] * (N - r)
    return hs


ans = solve()
print(len(ans))
print(*ans)
