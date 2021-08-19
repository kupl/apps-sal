import sys
from fractions import Fraction
(a, b, x, y) = list(map(int, sys.stdin.readline().strip().split()))
f = str(Fraction(x, y)).split('/')
if len(f) == 1:
    x = int(f[0])
    y = 1
else:
    x = int(f[0])
    y = int(f[1])
print(min(int(a / x), int(b / y)))
