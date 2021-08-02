from math import floor
from fractions import Fraction
a, b = input().split()
a = int(a)
b = Fraction(b)

print(floor(a * b))
