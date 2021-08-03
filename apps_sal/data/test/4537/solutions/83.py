import sys
import math

# https://atcoder.jp/contests/agc008/submissions/15248942
sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inm(): return map(int, sys.stdin.readline().split())
def inl(): return list(inm())
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

A, B = inm()
l = []
l.append(A + B)
l.append(A - B)
l.append(A * B)
print(max(l))
