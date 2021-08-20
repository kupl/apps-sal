import math
(a, b, h, m) = list(map(int, input().split()))
deg_m = m / 60 * 360
deg_h = (60 * h + m) / 720 * 360
deg = abs(deg_h - deg_m)
deg = math.radians(min(360 - deg, deg))
x2 = b ** 2 + a ** 2 - 2 * b * a * math.cos(deg)
print(x2 ** 0.5)
