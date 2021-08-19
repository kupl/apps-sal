import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7
INF = 10 ** 18
eps = 10 ** (-7)
(a, b) = map(int, input().split())
if a < 10 and b < 10:
    print(a * b)
else:
    print(-1)
