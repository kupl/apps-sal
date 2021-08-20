import math as m


class Point(object):

    def __init__(self, x, y, id):
        self.X = x
        self.Y = y
        self.id = id


def scalar(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2


def vector(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1


n = int(input())
dx2 = 0
dy2 = 0
a = []
for i in range(n):
    (x, y) = [int(j) for j in input().split()]
    a.append(Point(x, y, i + 1))
a.sort(key=lambda item: m.atan2(item.Y, item.X))
a.append(a[0])
minx = scalar(a[0].X, a[0].Y, a[1].X, a[1].Y)
miny = abs(vector(a[0].X, a[0].Y, a[1].X, a[1].Y))
(min1, min2) = (a[0].id, a[1].id)
for i in range(1, len(a)):
    dx2 = scalar(a[i - 1].X, a[i - 1].Y, a[i].X, a[i].Y)
    dy2 = abs(vector(a[i - 1].X, a[i - 1].Y, a[i].X, a[i].Y))
    if vector(dx2, dy2, minx, miny) > 0:
        (min1, min2) = (a[i - 1].id, a[i].id)
        minx = dx2
        miny = dy2
print(min1, min2)
"\nn = int(input())\nfor i in range(n):\n    x, y = input().split()\n    a.append(Point(int(x), int(y), i+1))\na.sort(key=lambda points: m.atan2(points.X, points.Y))\n''''''\nmindx = abs(scalar(a[0], a[n-1]))\nmindy = abs(vector(a[0], a[n-1]))\nnomber1 = a[0].id\nnomber2 = a[n-1].id\n\nfor i in range(n-1):\n    dx = abs(scalar(a[i], a[i+1]))\n    dy = abs(vector(a[i], a[i+1]))\n    if vectorCoordinate(dx, dy, mindy, mindx) > 0:\n        mindx = dx\n        mindy = dy\n        nomber1 = a[i].id\n        nomber2 = a[i+1].id\nprint(nomber2, nomber1)"
