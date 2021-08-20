import sys
from math import gcd
read = sys.stdin.buffer.read
x = 1
for n in range(1, 31):
    x = x // gcd(x, n) * n
print(x + 1)
