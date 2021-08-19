from math import ceil
(r, x0, y0, x1, y1) = map(int, input().split())
dist = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
print(ceil(dist / (2 * r)))
