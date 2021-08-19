(x1, y1, x2, y2) = map(int, input().split())
s = (x2 - x1 + 1) * ((y2 - y1 + 1) // 2) + (x2 - x1 + 2) // 2 * ((y2 - y1 + 1) % 2)
print(s)
