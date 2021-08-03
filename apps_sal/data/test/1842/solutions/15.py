from functools import reduce
from math import factorial
a, b, c = [int(x) for x in input().split()]
sq = (b**2 - 4 * a * c) ** 0.5
x, y = (-b + sq) / (2 * a), (-b - sq) / (2 * a)
if a < 0:
    x, y = y, x
print(x)
print(y)
