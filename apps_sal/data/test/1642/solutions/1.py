from math import hypot


n = int(input())


def square(a, b, c):
    first = [a[0] - c[0], a[1] - c[1]]
    second = [b[0] - c[0], b[1] - c[1]]
    return abs(first[0] * second[1] - first[1] * second[0])


def height(a, b, c):
    return square(a, b, c) / hypot(a[0] - b[0], a[1] - b[1])


points = []
for i in range(n):
    points.append(list(map(float, input().split())))
_max = 3e9

for i in range(n):
    a = points[i]
    b = points[(i + 1) % n]
    c = points[(i + 2) % n]
    _max = min(_max, (height(a, b, c) / 2))
    _max = min(_max, height(c, a, b) / 2)
    _max = min(_max, (height(b, c, a) / 2))

print(_max)
