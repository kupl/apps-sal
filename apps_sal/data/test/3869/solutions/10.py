from math import *
w, h, alpha = [int(x) for x in input().strip().split()]
if alpha > 90:
    alpha = 180 - alpha
if w < h:
    w, h = h, w
c = cos(alpha * pi / 180.0)
s = sin(alpha * pi / 180.0)
t = tan(alpha * pi / 360.0)

print(h * h / s) if t > h / w else print((w * h - (w * w + h * h) / 2 * tan(alpha * pi / 360.0)) / (c))
