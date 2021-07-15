x1, y1, x2, y2 = map(int, input().split())
a, b = (x2 - x1) // 2, (y2 - y1) // 2
print(a * b + (a + 1) * (b + 1))
