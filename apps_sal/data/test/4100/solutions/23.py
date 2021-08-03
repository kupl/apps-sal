import sys

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n, k, q = inl()
    A = [ini() - 1 for _ in range(q)]
    points = [k] * n
    for a in A:
        points[a] += 1
    for i in range(n):
        points[i] -= q
        print("Yes" if points[i] > 0 else "No")


solve()
