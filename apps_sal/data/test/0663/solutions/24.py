import math
r, x, y, x1, y1 = list(map(int, input().split()))
dist = ((x - x1)**2 + (y - y1)**2)**0.5
print(math.ceil(dist / (2 * r)))
