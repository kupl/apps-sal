import math
a, b, h, m = map(int, input().split())
# A: 360 / 720 [degree/min]
# B: 360/ 60 [degree/min]
r_a = 30 * h + 0.5 * m
r_b = 6 * m
rad = math.pi * (r_a - r_b) / 180
ans = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(rad))
print(ans)
