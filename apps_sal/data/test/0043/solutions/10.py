from collections import namedtuple
from math import sqrt
from functools import cmp_to_key
Vec = namedtuple("Vec", "x y index")
Fraction = namedtuple("Fraction", "num denom")

def fraction_comp(a, b):
    return a.num*b.denom > b.num*a.denom

def angle_comp(v):
    result = v.x / sqrt(v.x*v.x + v.y*v.y)
    if (v.y < 0):
        result = -2 - result
    return result

def angle(v1, v2):
    x1, y1 = v1.x, v1.y
    x2, y2 = v2.x, v2.y
    result = (x1*x2 + y1*y2) / (sqrt(x1*x1 + y1*y1)*sqrt(x2*x2 + y2*y2))
    sign = -1 if (x1*x2 + y1*y2) < 0 else 1
    return Fraction(sign*(x1*x2 + y1*y2)**2, (x1*x1 + y1*y1)*(x2*x2 + y2*y2))

n = int(input())

points = []
for i in range(n):
    x, y = tuple(map(int, input().split()))
    points.append(Vec(x, y, i))

points.sort(key=angle_comp)
points.reverse()

ans = (points[0].index + 1, points[n - 1].index + 1)
minAngleCos = angle(points[0], points[n - 1])

for i in range(n - 1):
    currAngleCos = angle(points[i], points[i + 1])
    if (fraction_comp(currAngleCos, minAngleCos)):
        minAngleCos = currAngleCos
        ans = (points[i].index + 1, points[i + 1].index + 1)

print(ans[0], ans[1], sep=' ')
