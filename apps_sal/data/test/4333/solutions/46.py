x, y, a, b = map(int, input().split())
dx, dy = a - x, b - y
c, d = a - dy, b + dx
e, f = c - dx, d - dy
print(c, d, e, f)
