from math import gcd
from bisect import *


class Point:

    def __init__(self, x, y):
        (self.x, self.y) = (x, y)

    def __add__(self, val):
        return Point(self.x + val.x, self.y + val.y)

    def __sub__(self, val):
        return Point(self.x - val.x, self.y - val.y)

    def __mul__(self, ratio):
        return Point(self.x * ratio, self.y * ratio)

    def __truediv__(self, ratio):
        return Point(self.x / ratio, self.y / ratio)

    @staticmethod
    def det(A, B):
        return A.x * B.y - A.y * B.x

    @staticmethod
    def dot(A, B):
        return A.x * B.x + A.y * B.y

    def onSegment(self, A, B):
        if self.det(B - A, self - A) != 0:
            return False
        if self.dot(B - A, self - A) < 0:
            return False
        if self.dot(A - B, self - B) < 0:
            return False
        return True


def intPoints(x1, y1, x2, y2):
    (dx, dy) = (abs(x2 - x1), abs(y2 - y1))
    return gcd(dx, dy) + 1


def crosspoint(L1, L2):
    (A, B) = (Point(L1[0], L1[1]), Point(L1[2], L1[3]))
    (C, D) = (Point(L2[0], L2[1]), Point(L2[2], L2[3]))
    (S1, S2) = (Point.det(C - A, D - A), Point.det(C - D, B - A))
    delta = (B - A) * S1
    if S2 == 0 or delta.x % S2 != 0 or delta.y % S2 != 0:
        return None
    delta = delta / S2
    P = A + delta
    if not P.onSegment(A, B) or not P.onSegment(C, D):
        return None
    return (P.x, P.y)


n = int(input())
lines = [tuple((int(z) for z in input().split())) for i in range(n)]
count = dict()
for i in range(n):
    for j in range(i):
        P = crosspoint(lines[i], lines[j])
        if P != None:
            count[P] = count.get(P, 0) + 1
answer = sum((intPoints(*L) for L in lines))
tri = [x * (x + 1) // 2 for x in range(n + 1)]
for z in count:
    k = bisect_right(tri, count[z])
    answer -= k - 1
print(answer)
