import math
(a, b, h, m) = map(int, input().split())
H = 30 * h + 0.5 * m
M = 6 * m
C = a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(H - M))
print(math.sqrt(C))
