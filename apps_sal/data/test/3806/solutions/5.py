import math


def main():
    (n, xp, yp) = (int(x) for x in input().split())
    polygon = [None] * n
    for i in range(n):
        (xi, yi) = (int(x) for x in input().split())
        polygon[i] = (xi, yi)
    print(solver((xp, yp), polygon))


def solver(P, polygon):
    n = len(polygon)
    (xp, yp) = P
    distances = [distance(xp, yp, x, y) for (x, y) in polygon]
    maxDist = max(distances)
    minDist = min(distances)
    for i in range(n):
        p = perpenPoint(polygon[i % n], polygon[(i + 1) % n], P)
        if p != None:
            dist = distance(xp, yp, p[0], p[1])
            if dist < minDist:
                minDist = dist
    area = math.pi * (maxDist**2 - minDist**2)
    return area


# ax + by = c
def toLine(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    if x1 == x2:
        if y1 == y2:
            assert(False)
        else:
            return (1, 0, x1)
    else:
        a = (y2 - y1) / (x1 - x2)
        c = a * x1 + y1
        return (a, 1, c)

# perpendicular point from point to the line segment: point1 to point3


def perpenPoint(point1, point2, point):
    line = toLine(point1, point2)
    (a, b, c) = line
    # perpendicular line
    if a == 0:
        (ap, bp) = (b, a)
    else:
        (ap, bp) = (-b / a, 1)
    (x, y) = point
    cp = ap * x + bp * y
    (xi, yi) = intersection(line, (ap, bp, cp))
    (x1, y1) = point1
    (x2, y2) = point2
    if min(x1, x2) <= xi and xi <= max(x1, x2) and \
            min(y1, y2) <= yi and yi <= max(y1, y2):
        return (xi, yi)
    else:
        return None


def intersection(line1, line2):
    (a1, b1, c1) = line1
    (a2, b2, c2) = line2
    if b1 == 0 and a2 == 0:
        return (c1, c2)
    elif a1 == 0 and b2 == 0:
        return (c2, c1)
    else:
        x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)
        y = (c1 - a1 * x) / b1
        return (x, y)


def almostEqual(x, y):
    return abs(x - y) < 10**-16


def distance(x1, y1, x2, y2):
    leg1 = abs(x1 - x2)
    leg2 = abs(y1 - y2)
    return (leg1**2 + leg2**2)**0.5


main()
#print(perpenPoint((-1, 0), (0, 1), (1.1, 0)))
#print(perpenPoint((-2, 0), (-2, 1), (0, 0)))
#print(perpenPoint((-1, 1), (2, 1), (0, 0)))
#print(perpenPoint((-1, 0), (1, 1), (0, 0)))
#print(12.56637061435 / math.pi)
#print(solver((0, 0), [(0, 1), (-1, 2), (1, 2)]))
#print(solver((1, -1), [(0, 0), (1, 2), (2, 0), (1, 1)]))
