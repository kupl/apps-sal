import sys
import math
def read(): return list(map(int, sys.stdin.readline().split()))


x1, y1, x2, y2 = read()
vmax, t1 = read()
vx, vy = read()
wx, wy = read()

x2, y2 = (x2 - x1) / vmax, (y2 - y1) / vmax
vx, vy, wx, wy = vx / vmax, vy / vmax, wx / vmax, wy / vmax

lo, up = 0, 10**9
for _ in range(100):
    t = (lo + up) / 2
    x = x2 - min(t, t1) * vx - max(t - t1, 0) * wx
    y = y2 - min(t, t1) * vy - max(t - t1, 0) * wy
    if x**2 + y**2 <= t**2:
        up = t
    else:
        lo = t

print(up)
