import math
(a, b, h, m) = map(int, input().split())
c = 2 * math.pi * (h * 60 + m) / 720
d = 2 * math.pi * (m / 60)
print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(c - d)))
