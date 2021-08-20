from math import *
(a, b, c) = map(float, input().split())
d = b * b - 4 * a * c
(x1, x2) = ((-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a))
print(max(x1, x2))
print(min(x1, x2))
