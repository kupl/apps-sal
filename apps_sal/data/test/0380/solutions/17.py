import math
def onsegment(x, y, z): return min(y, z) <= x <= max(y, z)
def oninterval(x, y, z): return min(y, z) < x < max(y, z)


def inrectangle(p0, p1, p2):
    return oninterval(p0[0], p1[0], p2[0]) and oninterval(p0[1], p1[1], p2[1])


def onborder(p0, p1, p2):
    return onsegment(p0[0], p1[0], p2[0]) and onsegment(p0[1], p1[1], p2[1]) and not inrectangle(p0, p1, p2)


points = []
for i in range(3):
    points.append(tuple(int(x) for x in input().split()))
points.sort()
if (all((point[0] == points[0][0] for point in points))
        or all((point[1] == points[0][1] for point in points))):
    print(1)
elif points[0][1] == points[2][1]:
    print(3 if points[0][0] < points[1][0] < points[2][0] else 2)
elif onborder(points[1], points[0], points[2]) or onborder(points[2], points[0], points[1]) or onborder(points[0], points[1], points[2]):
    print(2)
else:
    print(3)
