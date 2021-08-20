from math import radians, cos, sin, atan2


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


def intersect(a, b, c, d):
    r = crs(m(c, d), m(a, d)) * crs(m(c, d), m(b, d)) <= 0
    r &= crs(m(b, a), m(c, a)) * crs(m(b, a), m(d, a)) <= 0
    if not r:
        return None
    x1 = a[0]
    y1 = a[1]
    x2 = c[0]
    y2 = c[1]
    dx1 = b[0] - a[0]
    dx2 = d[0] - c[0]
    dy1 = b[1] - a[1]
    dy2 = d[1] - c[1]
    if dx2 * dy1 == dx1 * dy2:
        return None
    t = ((x1 - x2) * dy2 + (y2 - y1) * dx2) / (dx2 * dy1 - dx1 * dy2)
    return (x1 + t * dx1, y1 + t * dy1)


(w, h, alpha) = list(map(int, input().split()))
if alpha == 0 or alpha == 180:
    print(w * h)
else:
    alpha = radians(alpha)
    pnt = []
    pnt.append((w / 2, h / 2))
    pnt.append((-w / 2, h / 2))
    pnt.append((-w / 2, -h / 2))
    pnt.append((w / 2, -h / 2))
    pnt2 = []
    for p in pnt:
        pnt2.append(rotate(p, alpha))
    pnt2.append(pnt2[0])
    pnt.append(pnt[0])
    points_total = []
    for st in range(4):
        for en in range(4):
            t = intersect(pnt[st], pnt[st + 1], pnt2[en], pnt2[en + 1])
            if t != None:
                points_total.append(t)
    points_total = sorted(points_total, key=lambda x: atan2(x[1], x[0]))
    print(area(points_total))
