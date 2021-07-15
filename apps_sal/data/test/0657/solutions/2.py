import math
a, b = map(int, input().split())
x, y, z = map(int, input().split())

r = 2 * x + y
t = y + 3 * z
print(max(0, r - a) + max(0, t - b))
