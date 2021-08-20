import math
(a, b, h, m) = map(int, input().split())
q = abs(m / 60 - (h + m / 60) / 12) * 360
print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(q))))
