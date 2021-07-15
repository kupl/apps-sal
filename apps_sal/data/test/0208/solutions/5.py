3

import sys

x1, y1, x2, y2 = [int(x) for x in sys.stdin.readline().split()]

if x1 == x2:
    d = abs(y1 - y2)
    x3, y3 = x1 + d, y1
    x4, y4 = x1 + d, y2
elif y1 == y2:
    d = abs(x1 - x2)
    x3, y3 = x1, y1 + d
    x4, y4 = x2, y1 + d
elif abs(x1 - x2) != abs(y1 - y2):
    print('-1')
    return
else:
    xa, xb = min(x1, x2), max(x1, x2)
    ya, yb = min(y1, y2), max(y1, y2)
    points = [(xa, ya), (xa, yb), (xb, ya), (xb, yb)]
    (x3, y3), (x4, y4) = [p for p in points if p not in [(x1, y1), (x2, y2)]]

print(x3, y3, x4, y4)

