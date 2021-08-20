import math
(r, x1, y1, x2, y2) = input().split()
(r, x1, y1, x2, y2) = (float(r), float(x1), float(y1), float(x2), float(y2))
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
if d > r:
    print(x1, y1, r)
elif d == 0:
    print(x1 + r / 2, y1, r / 2)
else:
    R = (r + d) / 2
    dist = (r - d) / 2
    X = x1 - (x2 - x1) / d * dist
    Y = y1 - (y2 - y1) / d * dist
    print(X, Y, R)
