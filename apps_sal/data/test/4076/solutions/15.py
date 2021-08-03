import math as mt
a, b, h, m = list(map(int, input().split()))
print((mt.sqrt(a**2 + b**2 - 2 * a * b * mt.cos(2 * mt.pi * (1 / 12 * (h + m / 60) - m / 60)))))
