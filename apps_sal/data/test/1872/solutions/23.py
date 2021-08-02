from math import *

N, R = list(map(int, input().split()))


def get(i):
    theta = 2 * pi / N * i
    return R * cos(theta), R * sin(theta)


def line(p, q):
    m = (q[1] - p[1]) / (q[0] - p[0])
    b = p[1] - m * p[0]
    return (m, b)


def intersect(l1, l2):
    x = (l1[1] - l2[1]) / (l2[0] - l1[0])
    y = l1[0] * x + l1[1]
    return (x, y)


def dist(p, q):
    return sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)


p0 = get(0)
p1 = get(N // 2)

p2 = get(1)
p3 = get(N // 2 + 2)

p4 = intersect(line(p0, p1), line(p2, p3))

midpt = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2

h1 = dist(midpt, p4)
h2 = dist(midpt, (0, 0))

area = 0.5 * (h2 - h1) * dist(p0, p2)

print(area * N)
