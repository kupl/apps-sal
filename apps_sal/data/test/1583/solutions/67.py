import math
import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
INF = 10**18
eps = 10**-7

a, b, x = map(int, input().split())
v = a * a * b - x
maxh = v / (a * a) * 2
if maxh <= b:
    print(math.degrees(math.atan(maxh / a)))
else:
    maxh = 2 * x / (a * b)
    print(math.degrees(math.atan(b / maxh)))
