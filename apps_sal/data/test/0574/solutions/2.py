x1, y1, x2, y2 = map(int, input().split())
x = x2 - x1
y = y2 - y1
print((y // 2 + (y // 2 + 1)) * x // 2 + y // 2 + 1)
