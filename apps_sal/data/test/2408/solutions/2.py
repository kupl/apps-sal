import math


class Pt:

    def __init__(self, *args):
        if len(args) == 0:
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = list(map(int, args[0].split()))
        else:
            self.x, self.y = args[0], args[1]

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    def __add__(self, other):
        return Pt(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Pt(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Pt(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return Pt(self.x / other, self.y / other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    @staticmethod
    def get_straight(self, other):
        a = self.y - other.y
        b = other.x - self.x
        c = self.cross(other)
        return a, b, c


class Straight:

    def __init__(self, *args):
        if len(args) == 1:
            self.a, self.b, self.c = list(map(int, args[0].split()))
        elif len(args) == 2:
            self.a, self.b, self.c = Pt.get_straight(*args)
        elif len(args) == 3:
            self.a, self.b, self.c = args

    def __str__(self):
        return ' '.join(map(str, [self.a, self.b, self.c]))

    def __eq__(self, other):
        if self.b != 0 or other.b != 0:
            return self.a * other.b == other.a * self.b and self.c * other.b == other.c * self.b
        val1 = math.sqrt(self.a ** 2 + self.b ** 2)
        val2 = math.sqrt(other.a ** 2 + other.b ** 2)
        a1, c1 = self.a / val1, self.c / val1
        a2, c2 = other.a / val2, other.c / val2
        if (a1 < 0) != (a2 < 0):
            a1, a2, c1, c2 = a1, -a2, c1, -c2
        return a1 == a2 and c1 == c2

    def perpendicular(self, point: Pt):
        return Straight(-self.b, self.a, self.b * point.x - self.a * point.y)

    def get_value(self, point):
        return self.a * point.x + self.b * point.y + self.c

    def is_own(self, point: Pt):
        return self.get_value(point) == 0

    def same_side(self, pt1, pt2):
        return (self.get_value(pt1) < 0) == (self.get_value(pt2) < 0)

    def intersection(self, other):
        d = Pt(self.a, self.b).cross(Pt(other.a, other.b))
        dx = Pt(self.c, self.b).cross(Pt(other.c, other.b))
        dy = Pt(self.a, self.c).cross(Pt(other.a, other.c))
        return Pt(-dx / d, -dy / d)

    def dist_from_point(self, point):
        val = math.sqrt(self.a ** 2 + self.b ** 2)
        return abs(Straight(self.a / val, self.b / val, self.c / val).get_value(point))

    def parallel(self, dist):
        val = math.sqrt(self.a ** 2 + self.b ** 2)
        return Straight(self.a, self.b, self.c - dist * val)

    def is_parallel(self, other):
        return self.a * other.b == self.b * other.a

    def is_perpendicular(self, other):
        per = Straight(-self.b, self.a, 0)
        return per.a * other.b == per.b * other.a


n = int(input())
points = [Pt(input()) for _ in range(n)]
straights = []
for i in range(n):
    for j in range(i + 1, n):
        st = Straight(points[i], points[j])
        ok = True
        for x in straights:
            if st == x:
                ok = False
                break
        if ok:
            straights.append(st)
res = 0
m = len(straights)
for i in range(m):
    for j in range(i + 1, m):
        if not straights[i].is_parallel(straights[j]):
            res += 1
print(res)

