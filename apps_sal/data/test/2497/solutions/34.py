import sys
from scipy.optimize import fmin

input = sys.stdin.readline

n = int(input())

XR = []
XL = []
XS = []
YU = []
YD = []
YS = []

for _ in range(n):
    x, y, d = input().split()
    x = int(x)
    y = int(y)
    if d == "D":
        XS.append(x)
        YD.append(y)
    elif d == "U":
        XS.append(x)
        YU.append(y)
    elif d == "R":
        XR.append(x)
        YS.append(y)
    elif d == "L":
        XL.append(x)
        YS.append(y)


max_YD = max(YD + [float("-inf")])
max_YS = max(YS + [float("-inf")])
max_YU = max(YU + [float("-inf")])
min_YD = min(YD + [float("inf")])
min_YS = min(YS + [float("inf")])
min_YU = min(YU + [float("inf")])

max_XR = max(XR + [float("-inf")])
max_XL = max(XL + [float("-inf")])
max_XS = max(XS + [float("-inf")])
min_XR = min(XR + [float("inf")])
min_XL = min(XL + [float("inf")])
min_XS = min(XS + [float("inf")])


def diff_xy(t):
    diff_y = max(max_YD - t, max_YU + t, max_YS) - min(min_YD - t, min_YU + t, min_YS)
    diff_x = max(max_XL - t, max_XR + t, max_XS) - min(min_XL - t, min_XR + t, min_XS)
    return diff_x * diff_y


options = [
    max_YD - max_YS,
    max_YS - max_YU,
    (max_YD - max_YU) / 2,
    min_YD - min_YS,
    (min_YD - min_YU) / 2,
    min_YS - min_YU,
    max_XL - max_XS,
    max_XS - max_XR,
    (max_XL - max_XR) / 2,
    min_XL - min_XS,
    (min_XL - min_XR) / 2,
    min_XS - min_XR]

ans = diff_xy(0)

for option in options:
    if option >= 0:
        ans = min(ans, diff_xy(option))

print(ans)
