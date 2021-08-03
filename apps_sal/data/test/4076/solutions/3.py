import math
pi = math.pi
a, b, h, m = map(int, input().split())
ra = ((60 * h + m) / 360) * 180
rb = (180 / 30) * m
r = abs(ra - rb)
if r > 2 * 180:
    r = 2 * 180 - r
ans = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(r * 2 * pi / 360))
print(f'{ans:.20f}')
