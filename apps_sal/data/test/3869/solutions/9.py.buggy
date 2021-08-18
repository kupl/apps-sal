import math
from decimal import *
getcontext().prec = 40

EPS = Decimal(0.000000000000000000001)
PI = Decimal(3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328)


def labs(x):
    if x < 0:
        return -x
    return x


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Add(self, p):
        self.x += p.x
        self.y += p.y

    def Sub(self, p):
        self.x -= p.x
        self.y -= p.y

    def Scale(self, v):
        self.x *= v
        self.y *= v

    def Rotate(self, angle):
        newX = self.x * Decimal(math.cos(angle)) - self.y * Decimal(math.sin(angle))
        newY = self.x * Decimal(math.sin(angle)) + self.y * Decimal(math.cos(angle))
        self.x = newX
        self.y = newY

    def Equals(self, p):
        if Decimal(labs(p.x - self.x)) < EPS and Decimal(labs(p.y - self.y)) < EPS:
            return True
        return False


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def GetIntersection(self, l):
        a = Point(self.start.x, self.start.y)
        b = Point(self.end.x, self.end.y)
        c = Point(l.start.x, l.start.y)
        d = Point(l.end.x, l.end.y)
        ab = Point(self.end.x, self.end.y)
        cd = Point(l.end.x, l.end.y)
        ab.Sub(a)
        cd.Sub(c)
        k = Decimal((cd.x * (a.y - c.y) + cd.y * (c.x - a.x)) / (ab.x * cd.y - ab.y * cd.x))
        ab.Scale(k)
        a.Add(ab)
        return a


class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def GetArea(self):
        area = Decimal(0)
        for i in range(0, len(self.vertices)):
            area += self.vertices[i].x * self.vertices[(i + 1) % len(self.vertices)].y - self.vertices[(i + 1) % len(self.vertices)].x * self.vertices[i].y
        return Decimal(labs(area)) / Decimal(2)


x, y, alpha = input().split()
x = Decimal(x)
y = Decimal(y)
if x < y:
    tmp = x
    x = y
    y = tmp
alpha = Decimal(alpha)
singleArea = x * y
if alpha > 90:
    alpha = Decimal(180) - alpha
if alpha == 0:
    print(singleArea)
    return
alpha = alpha * PI / Decimal(180)
a = Point(x / Decimal(2), y / Decimal(2))
b = Point(x / Decimal(2), -y / Decimal(2))
c = Point(-x / Decimal(2), -y / Decimal(2))
d = Point(-x / Decimal(2), y / Decimal(2))
e = Point(a.x, a.y)
f = Point(b.x, b.y)
g = Point(c.x, c.y)
h = Point(d.x, d.y)
e.Rotate(alpha)
f.Rotate(alpha)
g.Rotate(alpha)
h.Rotate(alpha)
ab = Line(a, b)
bc = Line(b, c)
cd = Line(c, d)
da = Line(d, a)
ef = Line(e, f)
fg = Line(f, g)
gh = Line(g, h)
he = Line(h, e)
area = 0
if a.Equals(f):
    t1 = Polygon([he.GetIntersection(da), e, f])
    t2 = Polygon([fg.GetIntersection(bc), g, h])
    area = singleArea - t1.GetArea() - t2.GetArea()
elif f.y > a.y:
    p1 = Polygon([he.GetIntersection(da), e, f, fg.GetIntersection(da)])
    p2 = Polygon([fg.GetIntersection(bc), g, h, he.GetIntersection(bc)])
    area = singleArea - p1.GetArea() - p2.GetArea()
else:
    t1 = Polygon([da.GetIntersection(he), e, ef.GetIntersection(da)])
    t2 = Polygon([ef.GetIntersection(ab), f, fg.GetIntersection(ab)])
    t3 = Polygon([fg.GetIntersection(bc), g, gh.GetIntersection(bc)])
    t4 = Polygon([gh.GetIntersection(cd), h, he.GetIntersection(cd)])
    area = singleArea - t1.GetArea() - t2.GetArea() - t3.GetArea() - t4.GetArea()
print(area)
