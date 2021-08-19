def iscollinear(p1, p2, p3):
    (x1, y1) = p1
    (x2, y2) = p2
    (x3, y3) = p3
    cross = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    ans = bool(cross)
    return not ans


def checkfortwolines(a, b, points):
    set1 = set(points)
    for i in range(n):
        if iscollinear(a, b, points[i]):
            set1.remove(points[i])
    if len(set1) <= 2:
        return True
    else:
        pts1 = list(set1)
        for i in range(len(pts1)):
            if not iscollinear(pts1[0], pts1[1], pts1[i]):
                return False
        return True


n = int(input())
if n <= 4:
    print('YES')
else:
    points = [0 for i in range(n)]
    for i in range(n):
        points[i] = tuple(map(int, input().split()))
    a = points[0]
    b = points[1]
    c = points[2]
    if checkfortwolines(a, b, points) or checkfortwolines(b, c, points) or checkfortwolines(c, a, points):
        print('YES')
    else:
        print('NO')
