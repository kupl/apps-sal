import os
import sys
from collections import defaultdict

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

N = int(sys.stdin.readline())
X, Y = list(zip(*[list(map(int, sys.stdin.readline().split())) for _ in range(N)]))

yx = defaultdict(lambda: set())
xy = defaultdict(lambda: set())
for x, y in zip(X, Y):
    xy[x].add(y)
    yx[y].add(x)


def connected(x=None, y=None, xret=None, yret=None):
    xret = xret if xret else set()
    yret = yret if yret else set()

    if x is not None:
        for y in xy[x]:
            if y in yret:
                continue
            yret.add(y)
            xret, yret = connected(y=y, xret=xret, yret=yret)
    if y is not None:
        for x in yx[y]:
            if x in xret:
                continue
            xret.add(x)
            xret, yret = connected(x=x, xret=xret, yret=yret)

    return xret, yret


x_counted = set()
y_counted = set()

# X と Y の二部グラフで、連結であるすべての組に辺を張る
ans = 0
for x in list(xy.keys()):
    if x in x_counted:
        continue
    xs, ys = connected(x=x)
    # 辺数
    ans += len(xs) * len(ys)
    x_counted |= xs
    y_counted |= ys
# すでにある辺が重複してる
ans -= N
print(ans)

