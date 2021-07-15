class Point:
    x = 0.
    y = 0.

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def print(self):
        print(self.x, self.y)

def add(a, b):
    return Point(a.x + b.x, a.y + b.y)

def ln(a):
    return (a.x * a.x + a.y * a.y) ** 0.5

def norm(a):
    b = a
    l = ln(a)
    b.x /= l
    b.y /= l
    return b

def mult(a, b):
    return Point(a.x * b, a.y * b)

def rot(a):
    return Point(a.y, -a.x)

p = Point()
v = Point()
p.x, p.y, v.x, v.y, a, b, c, d = map(float, input().split())

v = norm(v)
r1 = add(p, mult(v, b))

v = rot(v)
r7 = add(p, mult(v, a / 2))
r6 = add(p, mult(v, c / 2))
v = rot(v)
r5 = add(r6, mult(v, d))
v = rot(v)
r2 = add(p, mult(v, a / 2))
r3 = add(p, mult(v, c / 2))
v = rot(rot(rot(v)))
r4 = add(r3, mult(v, d))


r1.print()
r2.print()
r3.print()
r4.print()
r5.print()
r6.print()
r7.print()

