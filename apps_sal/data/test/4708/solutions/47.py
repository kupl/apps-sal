import sys
import math

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inm(): return map(int, sys.stdin.readline().split())
def inl(): return list(inm())
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

N = ini()
K = ini()
X = ini()
Y = ini()

if N > K:
    print(K * X + (N - K) * Y)
else:
    print(N * X)
