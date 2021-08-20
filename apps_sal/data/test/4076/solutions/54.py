import math
(a, b, h, m) = map(int, input().split())
r_a = 30 * h + 0.5 * m
r_b = 6 * m
rad = math.pi * (r_a - r_b) / 180
ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(rad))
print(ans)
