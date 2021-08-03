x1, y1, x2, y2 = [int(x) for x in input().split()]
print((x2 - x1 + 1) * (y2 - y1 + 1) // 2 + ((y2 - y1) % 2 == 0))
