import math
(a, b, h, m) = map(int, input().split())
x = math.pi * h / 6 - math.pi * m / 30 + math.pi * m / 360
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(x))
print(c)
