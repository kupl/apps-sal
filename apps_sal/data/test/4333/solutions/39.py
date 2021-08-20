(x1, y1, x2, y2) = map(int, input().split())
d1 = x2 - x1
d2 = y2 - y1
print(x2 - d2, y2 + d1, x1 - d2, y1 + d1)
