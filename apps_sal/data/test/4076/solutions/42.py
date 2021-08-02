import math
a, b, h, m = map(int, input().split())
lrad = 6 * m
srad = 30 * h + 0.5 * m
if abs(lrad - srad) <= 180:
    do = abs(lrad - srad)
else:
    do = 360 - abs(lrad - srad)
rad = math.radians(do)
print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(rad)))
