from math import atan, degrees
(a, b, x) = map(int, input().split())
if x > 1 / 2 * b * a ** 2:
    w = 2 * (b / a - x / a ** 3)
else:
    w = a * b ** 2 / (2 * x)
print(degrees(atan(w)))
