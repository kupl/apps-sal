import sys
from fractions import gcd
my_file = sys.stdin
line = [int(i) for i in my_file.readline().split()]
a, b, c, d = line[0], line[1], line[2], line[3]
if a / b < c / d:
    N = (b * c) - (a * d)
    D = b * c
else:
    N = (a * d) - (b * c)
    D = a * d

dec = gcd(N, D)

print(N // dec, end="/")
print(D // dec)
