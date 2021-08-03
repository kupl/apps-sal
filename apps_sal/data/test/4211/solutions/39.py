import sys

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    B = inl()
    A = [None] * n
    A[0] = B[0]
    for i in range(1, n - 1):
        A[i] = min(B[i - 1], B[i])
    A[n - 1] = B[n - 2]
    return sum(A)


print(solve())
