from math import radians, cos, sin, atan2, sqrt, floor, acos


def rotate(point, alpha):
    x = point[0]
    y = point[1]
    return (x * cos(alpha) - y * sin(alpha), x * sin(alpha) + y * cos(alpha))


def crs(a, b):
    return a[0] * b[1] - a[1] * b[0]


def m(end, start):
    return (end[0] - start[0], end[1] - start[1])


def area(poly):
    ret = 0
    n = len(poly)
    for i in range(n):
        j = (i + 1) % n
        ret += crs(poly[i], poly[j])
    return abs(ret) / 2.0


def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def get_next_point(p0, p1, x, y):
    r = ((p1[0] - p0[0]) / x * y, (p1[1] - p0[1]) / x * y)
    r = rotate(r, radians(60))
    return (p1[0] + r[0], p1[1] + r[1])


a = list(map(int, input().split()))
pnt = [(0, 0), (a[0], 0)]
for i in range(1, len(a)):
    pnt.append(get_next_point(pnt[-2], pnt[-1], a[i - 1], a[i]))
    assert dist(pnt[-2], pnt[-1]) - a[i] <= 1e-07
ret = area(pnt) * 4 / sqrt(3)
for i in range(floor(ret), floor(ret) + 3):
    if abs(ret - i) < 1e-07:
        ret = i
print(ret)
