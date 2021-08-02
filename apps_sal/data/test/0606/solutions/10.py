import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if str(type(other)) == "<class 'int'>" or str(type(other)) == "<class 'float'>":
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __xor__(self, other):
        return self.x * other.y - other.x * self.y

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def get_nor(self):
        l = self.get_length()
        if l == 0:
            l = 1
        return Vector(self.x / l, self.y / l)

    def rotate(self):
        return Vector(-self.x, -self.y)


r, x, y, x1, y1 = list(map(float, input().split()))
if (x - x1) ** 2 + (y - y1) ** 2 < r ** 2:
    if x1 == x and y1 == y:
        v1 = Vector(r, 0)
    else:
        v1 = Vector(x1 - x, y1 - y).get_nor() * r
    v2 = v1.rotate()
    xp1 = x + v1.x
    yp1 = y + v1.y
    xp2 = x + v2.x
    yp2 = y + v2.y
    if (xp1 - x1) ** 2 + (yp1 - y1) ** 2 < (xp2 - x1) ** 2 + (yp2 - y1) ** 2:
        xp1 = xp2
        yp1 = yp2
    v3 = Vector(xp1 - x1, yp1 - y1) / 2
    ax = x1 + v3.x
    ay = y1 + v3.y
    print(ax, ay, v3.get_length())
else:
    print(x, y, r)
