(x1, y1, x2, y2) = list(map(int, input().split()))
print(((y2 - y1) // 2 + 1) * ((x2 - x1 + 2) // 2) + ((y2 - y1) // 2 + (y2 - y1) % 2) * ((x2 - x1 + 1) // 2))
