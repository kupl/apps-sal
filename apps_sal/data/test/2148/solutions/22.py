import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Curling:

    def __init__(self, r):
        self.r = r
        self.r2 = r * r
        self.d = r * 2
        self.disks = []
        self.results = []

    def add(self, x):
        min_y = [self.r]
        for disk in self.disks:  # type: Point
            x_distance = abs(x - disk.x)
            if x_distance == 0:
                min_y.append(disk.y + self.d)
            elif x_distance == self.d:
                min_y.append(disk.y)
            elif x_distance < self.d:
                min_y.append(self.calc_min_y(disk, x))
        disk = Point(x, max(min_y))
        self.disks.append(disk)
        self.results.append(str(disk.y))

    def calc_min_y(self, disk: Point, x):
        cx = abs(disk.x - x) / 2
        dy = math.sqrt(self.r2 - cx * cx)
        return disk.y + 2 * dy


[n, r] = list(map(int, input().split()))
curling = Curling(r)
x_positions = list(map(int, input().split()))
for x_position in x_positions:
    curling.add(x_position)
print(" ".join(curling.results))
