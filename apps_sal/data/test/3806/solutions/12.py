import functools


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def squared_distance(self, another_point):
        return (self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2


def point_segment_distance(p, a, b):
    ap = (p.x - a.x, p.y - a.y)
    ab = (b.x - a.x, b.y - a.y)
    bp = (p.x - b.x, p.y - b.y)

    indicator = (ap[0] * ab[0] + ap[1] * ab[1]) / (ab[0] ** 2 + ab[1] ** 2)
    if 0 < indicator < 1:
        return (ap[0] ** 2 + ap[1] ** 2) - indicator ** 2 * (ab[0] ** 2 + ab[1] ** 2)
    if indicator <= 0:
        return ap[0] ** 2 + ap[1] ** 2
    if indicator >= 1:
        return bp[0] ** 2 + bp[1] ** 2


class SnowBlower:
    def solution(self):
        first_line = input()
        first_line = first_line.split(" ")
        num_vertices = int(first_line[0])
        origin = Point(int(first_line[1]), int(first_line[2]))

        vertices = []
        for _ in range(num_vertices):
            point = input()
            point = point.split(" ")
            vertices.append(Point(int(point[0]), int(point[1])))

        max_distance = float("-inf")
        min_distance = float("inf")
        for vertex in vertices:
            squared_distance = origin.squared_distance(vertex)
            max_distance = squared_distance if squared_distance > max_distance else max_distance

        for i in range(num_vertices):
            distance = point_segment_distance(origin, vertices[i], vertices[i - 1])
            min_distance = distance if distance < min_distance else min_distance

        pi = 3.14159265358

        print(pi * (max_distance - min_distance))


def __starting_point():
    snow_blower = SnowBlower()
    snow_blower.solution()


__starting_point()
