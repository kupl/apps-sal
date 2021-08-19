import math
(a, b, h, m) = list(map(int, input().split()))
x = 6 * m
y = 30 * h + 0.5 * m
C = max(x, y) - min(x, y)
C = min(C, 360 - C)
print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(C))))
