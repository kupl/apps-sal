import sys
sys.setrecursionlimit(100000)
INF = 1000000000.0


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y
    return (x ** 2 + y ** 2) ** 0.5


def brute_force(point_set, left, right):
    min_dist = INF
    for i in range(left, right):
        for j in range(i + 1, right):
            min_dist = min(min_dist, distance(point_set[i], point_set[j]))
    return min_dist


def strip_closest(point_set, left, right, mid, dist_min):
    point_mid = point_set[mid]
    splitted_points = []
    for i in range(left, right):
        if abs(point_set[i].x - point_mid.x) <= dist_min:
            splitted_points.append(point_set[i])
    splitted_points.sort(key=lambda p: p.y)
    smallest = INF
    l = len(splitted_points)
    for i in range(0, l):
        for j in range(i + 1, l):
            if not splitted_points[j].y - splitted_points[i].y < dist_min:
                break
            d = distance(splitted_points[i], splitted_points[j])
            smallest = min(smallest, d)
    return smallest


def closest_util(point_set, left, right):
    if right - left <= 3:
        return brute_force(point_set, left, right)
    mid = (right + left) // 2
    dist_left = closest_util(point_set, left, mid)
    dist_right = closest_util(point_set, mid + 1, right)
    dist_min = min(dist_left, dist_right)
    return min(dist_min, strip_closest(point_set, left, right, mid, dist_min))


n = int(input())
a = list(map(int, input().split()))
point_set = []
for i in range(n):
    if i > 0:
        a[i] += a[i - 1]
    point_set.append(Point(i, a[i]))
point_set.sort(key=lambda a: a.x)
ans = closest_util(point_set, 0, n)
print('%.0f' % (ans * ans))
