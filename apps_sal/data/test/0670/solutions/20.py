from math import *


def r(x1, y1, x2, y2):
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5


a, b, c = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
r1 = abs(x1 - x2) + abs(y1 - y2)
if (a == 0 or b == 0):
    print(r1)
else:
    k = - a / b
    b = - c / b
    x01 = x1
    y01 = k * x1 + b
    x02 = (y2 - b) / k
    y02 = y2
    x03 = x2
    y03 = k * x2 + b
    x04 = (y1 - b) / k
    y04 = y1
    r2 = r(x1, y1, x01, y01) + r(x01, y01, x02, y02) + r(x02, y02, x2, y2)
    r3 = r(x1, y1, x01, y01) + r(x01, y01, x03, y03) + r(x03, y03, x2, y2)

    r12 = r(x1, y1, x04, y04) + r(x04, y04, x02, y02) + r(x02, y02, x2, y2)
    r13 = r(x1, y1, x04, y04) + r(x04, y04, x03, y03) + r(x03, y03, x2, y2)

    print(min(r1, r2, r3, r12, r13))
