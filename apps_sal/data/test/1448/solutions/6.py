import math
import sys
inf = 2000000000


class Point:
    (x, y) = (0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vec):
        return Point(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        self.x -= vec.x
        self.y -= vec.y

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    def dist_to_point(self, pA):
        return vector_by_points(self, pA).length()

    def dist_to_line(self, line):
        if math.sqrt(line.a * line.a + line.b * line.b) == 0:
            return inf
        return (self.x * line.a + self.y * line.b + line.c) / math.sqrt(line.a * line.a + line.b * line.b)

    def dist_to_segment(self, pA, pB):
        AB = vector_by_points(pA, pB)
        AC = vector_by_points(pA, self)
        if AB * AC < 0:
            return self.dist_to_point(pA)
        BA = -AB
        BC = vector_by_points(pB, self)
        if BA * BC < 0:
            return self.dist_to_point(pB)
        return abs(self.dist_to_line(line_by_points(pA, pB)))

    def dist_to_ray(self, pA, pB):
        AC = vector_by_points(pA, self)
        AB = vector_by_points(pA, pB)
        if AC * AB < 0:
            return self.dist_to_point(pA)
        return abs(self.dist_to_line(line_by_points(pA, pB)))


class Vector:
    (x, y) = (0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __mul__(self, vec):
        return self.x * vec.x + self.y * vec.y

    def __pow__(self, vec):
        return self.x * vec.y - self.y * vec.x

    def __truediv__(self, x):
        return Vector(self.x / x, self.y / x)

    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        return Vector(self.x - vec.x, self.y - vec.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    def normalize(self):
        ln = self.length()
        self.x /= ln
        self.y /= ln

    def to_len(self, x):
        self.normalize()
        self.x *= x
        self.y *= x

    def angle_rad(self, vec):
        angle = math.atan2(self ** vec, self * vec)
        if angle < 0:
            angle += 2 * math.pi
        return angle

    def angle(self, vec):
        return self.angle_rad(vec) / math.pi * 180

    def polar(self):
        return self.angle_rad(Vector(1, 0))


class Line:
    (a, b, c) = (0, 0, 0)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return str(self.a) + ' ' + str(self.b) + ' ' + str(self.c)

    def normalize(self):
        z = math.sqrt(self.a * self.a + self.b * self.b)
        self.a /= z
        self.b /= z
        self.c /= z

    def intersection(self, ln):
        opred = self.a * ln.b - self.b * ln.a
        opred_x = self.c * ln.b - self.b * ln.c
        opred_y = self.a * ln.c - self.c * ln.a
        x = -opred_x / opred
        y = -opred_y / opred
        return Point(x, y)


def vector_by_points(p1, p2):
    return Vector(p2.x - p1.x, p2.y - p1.y)


def normal_to_line(line):
    return Vector(line.a, line.b)


def line_by_points(p1, p2):
    b = p1.x - p2.x
    a = p2.y - p1.y
    c = -(a * p1.x + b * p1.y)
    return Line(a, b, c)


def segment_intersect(pA, pB, pC, pD):
    AB = vector_by_points(pA, pB)
    AC = vector_by_points(pA, pC)
    AD = vector_by_points(pA, pD)
    CD = vector_by_points(pC, pD)
    CB = vector_by_points(pC, pB)
    CA = -AC
    if AB ** AC * AB ** AD <= 0 and CD ** CB * CD ** CA <= 0 and (min(pC.x, pD.x) <= max(pA.x, pB.x) <= max(pC.x, pD.x) or min(pA.x, pB.x) <= max(pC.x, pD.x) <= max(pA.x, pB.x)):
        return True
    return False


def segment_to_segment(pA, pB, pC, pD):
    if segment_intersect(pA, pB, pC, pD):
        return 0
    mn = min(pA.dist_to_segment(pC, pD), pB.dist_to_segment(pC, pD))
    mn = min(mn, pC.dist_to_segment(pA, pB))
    mn = min(mn, pD.dist_to_segment(pA, pB))
    return mn


def ray_to_ray(pA, pB, pC, pD):
    pt = line_by_points(pA, pB).intersection(line_by_points(pC, pD))
    if pt.dist_to_ray(pA, pB) == 0 and pt.dist_to_ray(pC, pD) == 0:
        return 0
    return min(pA.dist_to_ray(pC, pD), pC.dist_to_ray(pA, pB))


def area(a):
    prev = Vector(a[-1].x, a[-1].y)
    ans = 0
    for pt in a:
        cur = Vector(pt.x, pt.y)
        ans += prev ** cur / 2
        prev = cur
    return abs(ans)


(n, d) = map(int, input().split())
field = [Point(0, d), Point(d, 0), Point(n, n - d), Point(n - d, n)]
s = area(field)
q = int(input())
for i in range(q):
    (x, y) = map(int, input().split())
    cur = Point(x, y)
    ar = area([field[0], field[1], cur]) + area([field[1], field[2], cur]) + area([field[2], field[3], cur]) + area([field[3], field[0], cur])
    if ar == s:
        print('YES')
    else:
        print('NO')
