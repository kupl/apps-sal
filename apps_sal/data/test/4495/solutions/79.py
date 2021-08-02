import math
import collections
from itertools import product

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

a, b, x = mi()

if a % x != 0:
    A = x * (a // x + 1)
else:
    A = a
B = b - b % x
print((B - A) // x + 1)
