import itertools
import math


def get_circle_center_and_radius(x1, y1, x2, y2, x3, y3):
    d = 2 * ((y1 - y3) * (x1 - x2) - (y1 - y2) * (x1 - x3))
    if d == 0:
        return (0, 0, 0)
    x = ((y1 - y3) * (y1 ** 2 - y2 ** 2 + x1 ** 2 - x2 ** 2) - (y1 - y2) * (y1 ** 2 - y3 ** 2 + x1 ** 2 - x3 ** 2)) / d
    y = ((x1 - x3) * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) - (x1 - x2) * (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2)) / -d
    r = (x - x1) ** 2 + (y - y1) ** 2
    return (x, y, r)


def get_circle_center_and_radius_two(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    r = (x - x1) ** 2 + (y - y1) ** 2
    return (x, y, r)


def check_if_all_included(x, y, r, points, v):
    for point in points:
        if point in v:
            continue
        dist = (x - point[0]) ** 2 + (y - point[1]) ** 2
        if dist > r:
            break
    else:
        return True
    return False


n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
r_min = 1000000
for v in itertools.combinations(points, 2):
    (x1, y1, x2, y2) = (v[0][0], v[0][1], v[1][0], v[1][1])
    (x, y, r) = get_circle_center_and_radius_two(x1, y1, x2, y2)
    if check_if_all_included(x, y, r, points, v) and r < r_min:
        r_min = r
for v in itertools.combinations(points, 3):
    (x1, y1, x2, y2, x3, y3) = (v[0][0], v[0][1], v[1][0], v[1][1], v[2][0], v[2][1])
    (x, y, r) = get_circle_center_and_radius(x1, y1, x2, y2, x3, y3)
    if r == 0:
        continue
    if check_if_all_included(x, y, r, points, v) and r < r_min:
        r_min = r
print(math.sqrt(r_min))
