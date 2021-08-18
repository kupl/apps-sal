import math
a, b, h, m = map(float, input().split())
c = abs(30 * h - 11 / 2 * m)
ct = math.radians(c)
cos = math.cos(ct)
ans = a**2 + b**2 - 2 * a * b * cos
print(math.sqrt(ans))
