import math
(a, b, h, m) = map(int, input().split())
t = math.pi * (60 * h - 11 * m) / 360
l = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(t))
print(l)
