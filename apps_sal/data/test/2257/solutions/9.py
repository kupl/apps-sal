import math


def dist(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2


n, x1, y1, x2, y2 = [int(x) for x in input().split()]
p1, p2 = (x1, y1), (x2, y2)
flowers = []

for _ in range(n):
    x, y = [int(x) for x in input().split()]
    flowers.append((x, y))

d1 = list(sorted(list(range(n)), key=lambda i: dist(flowers[i], p1)))
d2 = list(sorted(list(range(n)), key=lambda i: dist(flowers[i], p2)))
d2_1 = [0] * n
for i, d in enumerate(d2):
    d2_1[d] = i

dst = dist(flowers[d2[-1]], p2)
ptr = len(d2) - 1
for d in d1:
    d2[d2_1[d]] = None
    dist1 = dist(flowers[d], p1)
    while d2[ptr] is None and ptr >= 0:
        ptr -= 1
    if ptr >= 0:
        dist2 = dist(flowers[d2[ptr]], p2)
    else:
        dist2 = 0
    if dst is None or dist1 + dist2 < dst:
        dst = dist1 + dist2

print(dst)
