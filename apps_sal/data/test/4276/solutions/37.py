import sys
import math

# https://atcoder.jp/contests/agc008/submissions/15248942
sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inm(): return map(int, sys.stdin.readline().split())
def inl(): return list(inm())
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

N, T = inm()
min_cost = 2000

for i in range(N):
    c, t = inm()
    if t <= T:
        min_cost = min(min_cost, c)

if min_cost == 2000:
    print("TLE")
else:
    print(min_cost)
