x1, y1, x2, y2 = map(int, input().split())
x4 = x1 + y1 - y2
y4 = y1 + x2 - x1
x3 = x4 - y1 + y4
y3 = y4 + x1 - x4
print(x3, y3, x4, y4)
