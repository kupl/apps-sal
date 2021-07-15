import math

EPSILON = 10 ** -3


class Vector:
    def __init__(self, d=2, coords=[0, 0]):
        self.d = d
        self.coords = coords[:]

    @staticmethod
    def fromEnds(p1, p2):
        n = len(p1)
        assert n == len(p2)
        v = []
        for i in range(n):
            v.append(p2[i] - p1[i])
        return Vector(n, v)

    def apply(self, point):
        return tuple([self.coords[i] + point[i] for i in range(self.d)])

    def inverse(self):
        return Vector(self.d, list(map((lambda x: -x), self.coords)))

    def __repr__(self):
        return "Vector[{}] ({})".format(self.d, self.coords)

    def len(self):
        return math.sqrt(sum(x * x for x in self.coords))

    def __add__(self, other):
        assert self.d == other.d
        return Vector(self.d, [self.coords[i] + other.coords[i] for i in range(self.d)])

    def __eq__(self, other):
        return self.d == other.d and self.coords == other.coords

    def extend(self, k):
        return Vector(self.d, [x * k for x in self.coords])

    def scalmul(self, other):
        assert self.d == other.d
        return sum(self.coords[i] * other.coords[i] for i in range(self.d))

    def cos(self, other):
        return self.scalmul(other) / (self.len() * other.len())

    def is_ort(self, other):
        return self.scalmul(other) <= EPSILON

    def proj_to(self, other):
        return self.scalmul(other) / other.len()

    def proj_from(self, other):
        return other.proj_to(self)


t = lambda: tuple(map(int, input().split()))
p1, p2, p3 = t(), t(), t()
p = [p1, p2, p3]
ans = set()
for i in range(3):
    others = []
    for _p in p:
        if _p != p[i]:
            others.append(_p)

    assert len(others) == 2
    v1 = Vector.fromEnds(others[0], others[1])
    v2 = Vector.fromEnds(others[1], others[0])
    ans.add(v1.apply(p[i]))
    ans.add(v2.apply(p[i]))

print(len(ans))
for item in ans:
    print(" ".join(map(str,item)))
