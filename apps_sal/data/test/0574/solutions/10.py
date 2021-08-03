x1, y1, x2, y2 = [int(i) for i in input().split()]

t = y2 - y1 + 1
h = (x2 - x1 + 2) // 2

print(t // 2 * (h - 1) + (t // 2 + t % 2) * h)
