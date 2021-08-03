import sys

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    k, n = inl()
    A = inl()
    dmax = A[0] + (k - A[-1])
    for i in range(1, n):
        dmax = max(dmax, A[i] - A[i - 1])
    return k - dmax


print(solve())
