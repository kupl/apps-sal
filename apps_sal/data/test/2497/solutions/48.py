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
    (x, y, d) = input().split()
    x = int(x)
    y = int(y)
    if d == 'D':
        XS.append(x)
        YD.append(y)
    elif d == 'U':
        XS.append(x)
        YU.append(y)
    elif d == 'R':
        XR.append(x)
        YS.append(y)
    elif d == 'L':
        XL.append(x)
        YS.append(y)
max_YD = max(YD + [float('-inf')])
max_YS = max(YS + [float('-inf')])
max_YU = max(YU + [float('-inf')])
min_YD = min(YD + [float('inf')])
min_YS = min(YS + [float('inf')])
min_YU = min(YU + [float('inf')])
max_XR = max(XR + [float('-inf')])
max_XL = max(XL + [float('-inf')])
max_XS = max(XS + [float('-inf')])
min_XR = min(XR + [float('inf')])
min_XL = min(XL + [float('inf')])
min_XS = min(XS + [float('inf')])


def diff_xy(t):
    if t < 0:
        return float('inf')
    diff_y = max(max_YD - t, max_YU + t, max_YS) - min(min_YD - t, min_YU + t, min_YS)
    diff_x = max(max_XL - t, max_XR + t, max_XS) - min(min_XL - t, min_XR + t, min_XS)
    return diff_x * diff_y


def binary_search(min_t, max_t):
    mid_t = (min_t + max_t) / 2
    if max_t - min_t < 10 ** (-10):
        return diff_xy(mid_t)
    if diff_xy(min_t) < diff_xy(mid_t):
        return binary_search(min_t, mid_t)
    elif diff_xy(max_t) < diff_xy(mid_t):
        return binary_search(mid_t, max_t)
    else:
        return opt(min_t, mid_t, max_t)


def opt(a, b, c):
    optimal_a = fmin(diff_xy, a, full_output=False, disp=False, xtol=10 ** (-10))
    optimal_b = fmin(diff_xy, b, full_output=False, disp=False, xtol=10 ** (-10))
    optimal_c = fmin(diff_xy, c, full_output=False, disp=False, xtol=10 ** (-10))
    ans = min(diff_xy(optimal_a[0]), diff_xy(optimal_b[0]), diff_xy(optimal_c[0]))
    return ans


print(binary_search(0, 2 * 10 ** 8))
