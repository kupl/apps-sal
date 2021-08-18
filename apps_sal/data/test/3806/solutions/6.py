__author__ = 'vboldovs'


import math

GLOBAL_INNER_PRODUCT_LIMIT = math.pow(10, -3)


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class line:
    def __init__(self, start_point, end_point):
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y


def distance(p1, p2):
    return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))


def product(line1, line2):
    return line1.x * line2.x + line1.y * line2.y


m = input().split()
n = int(m[0])
center = point(int(m[1]), int(m[2]))

points = []

for _i in range(n):
    temp = input().split()
    points.append(point(int(temp[0]), int(temp[1])))

max_r = distance(center, points[0])
min_r = max_r

for p in points:
    d = distance(p, center)
    max_r = max(max_r, d)
    min_r = min(min_r, d)

for i in range(n):
    s_point = points[i]
    try:
        e_point = points[i + 1]
    except IndexError:
        e_point = points[0]
    curr_line = line(s_point, e_point)

    prod_s = product(curr_line, line(s_point, center))
    prod_e = product(curr_line, line(e_point, center))

    if prod_s * prod_e > 0:
        continue

    alpha = prod_s / abs(prod_e - prod_s)
    p_point = point((1 - alpha) * s_point.x + alpha * e_point.x, (1 - alpha) * s_point.y + alpha * e_point.y)

    min_r = min(min_r, distance(p_point, center))


print(math.pi * math.pow(max_r, 2) - math.pi * math.pow(min_r, 2))
