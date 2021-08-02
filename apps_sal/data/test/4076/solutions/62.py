import math
a, b, H, M = map(int, input().split())
h = 30 * H + (0.5) * M
m = 6 * M
c = abs(h - m)
x = math.sqrt(a**2 + b**2 - (2 * a * b * (math.cos(math.radians(c)))))
print(x)
