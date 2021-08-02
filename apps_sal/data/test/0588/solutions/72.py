import math
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N = int(sys.stdin.readline())
XY = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def calc(bx, by):
    base = math.atan2(bx, by)

    d1 = []
    d2 = []
    for x, y in XY:
        deg = (math.atan2(x, y) - base) % (math.pi * 2)
        if deg < math.pi:
            d1.append((x, y))
        else:
            d2.append((x, y))

    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    for x, y in d1:
        x1 += x
        y1 += y
    for x, y in d2:
        x2 += x
        y2 += y

    return max(math.sqrt(x1 ** 2 + y1 ** 2), math.sqrt(x2 ** 2 + y2 ** 2))


ans = 0
for x, y in XY:
    ans = max(ans, calc(x, y))
print(ans)
