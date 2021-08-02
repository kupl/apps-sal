x1, y1, x2, y2 = map(int, input().split())
a = x1 - x2
b = y1 - y2
print(x2 + b, y2 - a, x1 + b, y1 - a)
