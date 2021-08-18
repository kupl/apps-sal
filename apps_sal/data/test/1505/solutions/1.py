import math
3


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.hypot(self.x, self.y)

    def normalize(self):
        self /= self.length()

    def normalized(self):
        return self / self.length()

    def rotateLeft(self):
        x = self.x
        y = self.y
        self.x = -y
        self.y = x

    def rotatedLeft(self):
        x = -self.y
        y = self.x
        return Vector(x, y)

    def rotateRight(self):
        x = self.x
        y = self.y
        self.x = y
        self.y = -x

    def rotatedRight(self):
        x = self.y
        y = -self.x
        return Vector(x, y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        return self

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)


px, py, vx, vy, a, b, c, d = [int(i) for i in input().split()]

LEFT = math.pi * 0.5
RIGHT = -math.pi * 0.5
BACK = math.pi

p = Vector(px, py)
v = Vector(vx, vy)

v.normalize()

A = p + v * b
B = p + v.rotatedLeft() * (a / 2)
C = p + v.rotatedLeft() * (c / 2)
D = C + (-v) * d
F = p + v.rotatedRight() * (c / 2)
E = F + (-v) * d
G = p + v.rotatedRight() * (a / 2)

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
