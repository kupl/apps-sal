import math


def dist(a, b, c):
    return abs((c[1] - a[1]) * b[0] - (c[0] - a[0]) * b[1] + c[0] * a[1] - c[1] * a[0]) / math.hypot(c[0] - a[0], c[1] - a[1])


N = int(input())
pts = [tuple(map(int, input().split())) for _ in range(N)]
MIN = 10000000000.0
for i in range(N - 2):
    MIN = min(MIN, dist(pts[i], pts[i + 1], pts[i + 2]))

MIN = min(MIN, dist(pts[N - 2], pts[N - 1], pts[0]))
MIN = min(MIN, dist(pts[N - 1], pts[0], pts[1]))
print(MIN / 2)
