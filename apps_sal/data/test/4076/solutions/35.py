import math
a, b, h, m = (float(x) for x in input().split())
x = (h * math.pi / 6) + (m * math.pi / 360)
y = (m * math.pi / 30)
print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(x - y)))
