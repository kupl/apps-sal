from functools import reduce
from math import factorial
l1, l2, l3 = [int(x) for x in input().split()]
A = (2**0.5) / 12
B = ((15 + 5 * 5**0.5) / 288)**0.5
print((l1**3 + 2 * l2**3) * A + B * l3**3)
