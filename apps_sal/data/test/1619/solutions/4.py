from math import gcd, sqrt
from functools import reduce
import sys

input = sys.stdin.readline

EPS = 0.000000001


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def GCD(args):
    return reduce(gcd, args)


def plane_value(plane, point):
    A, B, C, D = plane
    x, y, z = point
    return A * x + B * y + C * z + D


def plane(p1, p2, p3):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    a1, b1, c1 = x2 - x1, y2 - y1, z2 - z1
    a2, b2, c2 = x3 - x1, y3 - y1, z3 - z1
    a, b, c = b1 * c2 - b2 * c1, a2 * c1 - a1 * c2, a1 * b2 - b1 * a2
    d = (- a * x1 - b * y1 - c * z1)
    g = GCD([a, b, c, d])
    return a // g, b // g, c // g, d // g


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def intersection_of_two_planes(p1, p2):
    A1, B1, C1, D1 = p1
    A2, B2, C2, D2 = p2

    crossprod = cross([A1, B1, C1], [A2, B2, C2])

    if (A1 * B2 - A2 * B1) != 0:
        x = ((B1 * D2 - B2 * D1) / (A1 * B2 - A2 * B1), crossprod[0])
        y = ((A2 * D1 - A1 * D2) / (A1 * B2 - A2 * B1), crossprod[1])
        z = (0, crossprod[2])
    elif (B1 * C2 - B2 * C1) != 0:
        x = (0, crossprod[0])
        y = ((C1 * D2 - C2 * D1) / (B1 * C2 - B2 * C1), crossprod[1])
        z = ((B2 * D1 - B1 * D2) / (B1 * C2 - B2 * C1), crossprod[2])
    elif (A1 * C2 - A2 * C1) != 0:
        x = ((C1 * D2 - C2 * D1) / (A1 * C2 - A2 * C1), crossprod[0])
        y = (0, crossprod[1])
        z = ((A2 * D1 - A1 * D2) / (A1 * C2 - A2 * C1), crossprod[2])
    else:
        return None

    return x, y, z


def line_parametric(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x2, x1 - x2), (y2, y1 - y2), (z2, z1 - z2)


def solve_2_by_2(row1, row2):
    a1, b1, c1 = row1
    a2, b2, c2 = row2
    if a1 * b2 - b1 * a2:
        return (c1 * b2 - b1 * c2) / (a1 * b2 - b1 * a2), (a1 * c2 - c1 * a2) / (a1 * b2 - b1 * a2)
    else:
        return None


def sgn(x):
    return 1 if x > 0 else 0 if x == 0 else -1


def lines_intersection_point(i1, i2):
    x1, y1, z1 = i1
    x2, y2, z2 = i2

    try:
        t1, t2 = solve_2_by_2([x1[1], -x2[1], x2[0] - x1[0]], [y1[1], -y2[1], y2[0] - y1[0]])
        if abs(t1 * z1[1] - t2 * z2[1] - z2[0] + z1[0]) < EPS:
            return (x1[0] + t1 * x1[1], y1[0] + t1 * y1[1], z1[0] + t1 * z1[1]), t2
        else:
            return None
    except:
        try:
            t1, t2 = solve_2_by_2([x1[1], -x2[1], x2[0] - x1[0]], [z1[1], -z2[1], z2[0] - z1[0]])
            if abs(t1 * y1[1] - t2 * y2[1] - y2[0] + y1[0]) < EPS:
                return (x1[0] + t1 * x1[1], y1[0] + t1 * y1[1], z1[0] + t1 * z1[1]), t2
            else:
                return None
        except:
            try:
                t1, t2 = solve_2_by_2([y1[1], -y2[1], y2[0] - y1[0]], [z1[1], -z2[1], z2[0] - z1[0]])
                if abs(t1 * x1[1] - t2 * x2[1] - x2[0] + x1[0]) < EPS:
                    return (x1[0] + t1 * x1[1], y1[0] + t1 * y1[1], z1[0] + t1 * z1[1]), t2
                else:
                    return None
            except:
                return None


def foo(points):
    down_cnt, up_cnt = 0, 0
    first = points[0]
    other = 1 - first
    down = True
    intrusion = True
    for p in points[1:]:
        if p == first:
            intrusion = not intrusion
        else:
            if intrusion:
                if down:
                    down_cnt += 1
                else:
                    up_cnt += 1
            down = not down
    return down_cnt == up_cnt


def populate(plane, poly, tag):
    res = []
    prev = plane_value(plane, poly[-1])
    prev_serious = plane_value(plane, poly[-2]) if not prev else prev
    p_prev = poly[-1]
    for i in range(len(poly) + 1):
        p = poly[i % len(poly)]
        curr = plane_value(plane, p)
        if sgn(curr) == -sgn(prev_serious):
            intersector = line_parametric(p_prev, p)
            point, t = lines_intersection_point(intersector, intersectee)
            res.append((t, tag))
            prev_serious = curr
        if sgn(curr):
            prev_serious = curr
        prev, p_prev = curr, p
    return res


x_poly, y_poly = [], []

for _ in range(inp()):
    x_poly.append(inlt())
for _ in range(inp()):
    y_poly.append(inlt())

x_plane = plane(*x_poly[:3])
y_plane = plane(*y_poly[:3])

intersectee = intersection_of_two_planes(x_plane, y_plane)

if intersectee:
    points = sorted(set(populate(y_plane, x_poly, 0) + populate(x_plane, y_poly, 1)))
    points = [i[1] for i in points]

    print('NO' if foo(points) else 'YES')
else:
    print('NO')
