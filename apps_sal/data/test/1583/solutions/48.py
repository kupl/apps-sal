from math import degrees, atan
(a, b, x) = map(int, input().split())
if a * a * b < x * 2:
    c = 2 * (a * a * b - x) / a ** 3
else:
    c = a * b * b / (2 * x)
print(degrees(atan(c)))
