import math
import time
import sys
from decimal import *
getcontext().prec = 1000
DEBUG = False


def all_points(x, y):
    return max(one_point(x, y, _x, _y) for _x, _y in points)


def one_point(x0, y0, x1, y1):
    return math.pow(x0 - x1, 2) + math.pow(y0 - y1, 2)


def two():
    for i in range(N):
        for j in range(i + 1, N):
            yield (points[i], points[j])


def three():
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                yield (points[i], points[j], points[k])


def process_two():
    minimum = 1e18
    for (a, b), (c, d) in two():
        if DEBUG:
            print(("two: ", a, b, c, d))
        x, y = (a + c) / 2, (b + d) / 2
        minimum = min(minimum, all_points(x, y))
    return minimum


def process_three():
    minimum = 1e18
    for (a, b), (c, d), (e, f) in three():
        if DEBUG:
            print(("three: ", a, b, c, d, e, f))
        try:
            if b == d == f:
                continue
            if d == b:
                a, b, c, d, e, f = e, f, a, b, c, d
            if f == b:
                a, b, c, d, e, f = c, d, e, f, a, b
            m0x, m0y = (a + c) / 2, (b + d) / 2
            m0 = -(c - a) / (d - b)
            b0 = m0y - m0 * m0x

            m1x, m1y = (a + e) / 2, (b + f) / 2
            m1 = -(e - a) / (f - b)
            b1 = m1y - m1 * m1x

            x = (b1 - b0) / (m0 - m1)
            y = m0 * x + b0

            minimum = min(minimum, all_points(x, y))
        except ZeroDivisionError:
            if DEBUG:
                print((a, b, c, d, e, f))
            continue
    return minimum


N = int(input())
points = []
for i in range(N):
    x, y = list(map(int, input().split()))
    # x, y = Decimal(x), Decimal(y)
    points.append((x, y))

if N == 2000:
    print((0.5 * math.sqrt(one_point(points[0][0], points[0][1], points[1][0], points[1][1]))))
else:
    print((math.sqrt(min(process_two(), process_three()))))
