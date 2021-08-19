import sys
import math

# https://atcoder.jp/contests/agc008/submissions/15248942
sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inm(): return map(int, sys.stdin.readline().split())
def inl(): return list(inm())
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

x1, y1, x2, y2 = inm()

y3 = y2 + (x2 - x1)
x3 = x2 - (y2 - y1)
y4 = y3 - (y2 - y1)
x4 = x3 - (x2 - x1)

print(x3, y3, x4, y4)
