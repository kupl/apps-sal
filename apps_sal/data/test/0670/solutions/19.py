from math import *
(a, b, c) = list(map(int, input().split()))
(x1, y1, x2, y2) = list(map(int, input().split()))
d = abs(x1 - x2) + abs(y1 - y2)
if a != 0 and b != 0:
    dy1 = abs(x1 + (c + b * y1) / a)
    dx1 = abs(y1 + (c + a * x1) / b)
    yy1 = y1
    xy1 = -(c + b * y1) / a
    xx1 = x1
    yx1 = -(c + a * x1) / b
    dy2 = abs(x2 + (c + b * y2) / a)
    dx2 = abs(y2 + (c + a * x2) / b)
    yy2 = y2
    xy2 = -(c + b * y2) / a
    xx2 = x2
    yx2 = -(c + a * x2) / b
    d1 = dy1 + dy2 + sqrt((xy1 - xy2) ** 2 + (yy1 - yy2) ** 2)
    d2 = dx1 + dx2 + sqrt((xx1 - xx2) ** 2 + (yx1 - yx2) ** 2)
    d3 = dy1 + dx2 + sqrt((xy1 - xx2) ** 2 + (yy1 - yx2) ** 2)
    d4 = dx1 + dy2 + sqrt((xx1 - xy2) ** 2 + (yx1 - yy2) ** 2)
    print(min(d, d1, d2, d3, d4))
else:
    print(d)
