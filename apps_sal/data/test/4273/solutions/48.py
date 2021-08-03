import sys
from collections import Counter

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    S = [ins() for _ in range(n)]
    c = Counter()
    M = "MARCH"
    for x in S:
        if x[0] in M:
            c[x[0]] += 1
    ans = 0
    for i in range(5):
        for j in range(i):
            for k in range(j):
                ans += c[M[i]] * c[M[j]] * c[M[k]]
    return ans


print(solve())
