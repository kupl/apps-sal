x1, y1, x2, y2 = map(int, input().split())

x = (x2 - x1) // 2
y = (y2 - y1) // 2

print(2 * x * y + x + y + 1)
