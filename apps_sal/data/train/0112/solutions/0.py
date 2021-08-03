import math


def lexComp(a, b):
    if a[0] != b[0]:
        return -1 if a[0] < b[0] else 1
    if a[1] != b[1]:
        return -1 if a[1] < b[1] else 1
    return 0


def turn(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])


def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def solve(n):
    a = [list(map(int, input())) for _ in range(n)]
    points = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                curPoints = []
                for dx in range(0, 2):
                    for dy in range(0, 2):
                        ok = True
                        for ddx in range(0, 2):
                            for ddy in range(0, 2):
                                x, y = i - 1 + dx + ddx, j - 1 + dy + ddy
                                if 0 <= x < n and 0 <= y < n and a[x][y] == 0:
                                    ok = False
                        if ok:
                            curPoints.append((i + dx, j + dy))
                points.append(curPoints[0])
    points = list(set(points))
    for i in range(1, len(points)):
        if lexComp(points[0], points[i]) > 0:
            points[0], points[i] = points[i], points[0]
    points[1:] = sorted(points[1:], key=lambda p: (math.atan2(p[1] - points[0][1], p[0] - points[0][0]), dist2(p, points[0])))
    hull = []
    for p in points:
        while len(hull) >= 2 and turn(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    hull = [(p[1], n - p[0]) for p in hull]
    hull = hull[::-1]
    start = 0
    for i in range(1, len(hull)):
        if lexComp(hull[i], hull[start]) < 0:
            start = i
    newHull = hull[start:]
    newHull.extend(hull[:start])
    hull = newHull
    print(len(hull))
    for p in hull:
        print(p[0], p[1])


while True:
    n = int(input())
    if n == 0:
        break
    solve(n)
