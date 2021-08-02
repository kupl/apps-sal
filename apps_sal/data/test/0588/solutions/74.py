from math import sqrt
n = int(input())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return

    def __lt__(self, p2):
        return self.quadrant() < p2.quadrant() or self.quadrant() == p2.quadrant() and self.x * p2.y - self.y * p2.x > 0

    def __repr__(self):
        return repr((self.x, self.y))

    def __add__(self, p2):
        return Point(self.x + p2.x, self.y + p2.y)

    def __sub__(self, p2):
        return Point(self.x - p2.x, self.y - p2.y)

    def quadrant(self):
        if self.x > 0 and self.y >= 0:
            return 1
        elif self.y > 0:
            return 2
        elif self.x < 0:
            return 3
        else:
            return 4

    def square(self):
        return self.x ** 2 + self.y ** 2


xy = [Point(xi, yi) for xi, yi in (list(map(int, input().split())) for _ in range(n)) if not xi == yi == 0]


cur_point = sum((p for p in xy if p.y > 0 or p.y == 0 and p.x >= 0), Point(0, 0))

inv = list(Point(-p.x, -p.y) for p in xy)
xy.extend(inv)
xy.sort()

mx = cur_point.square()
for p in xy:
    cur_point -= p
    mx = max(mx, cur_point.square())

print((sqrt(mx)))
