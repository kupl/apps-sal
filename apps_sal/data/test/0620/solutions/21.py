class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def f(a, b, p):
    dx = a.x - p.x
    dy = a.y - p.y
    return Point(b.x + dx, b.y + dy)


l = []
for _ in range(3):
    l.append(Point(*list(map(int, input().split()))))
answ = []
answ.append(f(l[0], l[1], l[2]))
answ.append(f(l[0], l[2], l[1]))
answ.append(f(l[1], l[2], l[0]))
print(len(answ))
for i in answ:
    print(i.x, i.y)
