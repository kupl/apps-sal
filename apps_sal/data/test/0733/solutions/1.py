import math
import sys
from fractions import gcd
(x, y, a, b) = list(map(int, sys.stdin.readline().split()))
g = x * y // gcd(x, y)
s = math.ceil(a / g)
e = math.floor(b / g)
print(e - s + 1)
