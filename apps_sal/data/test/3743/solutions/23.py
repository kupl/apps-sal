"""input
5
"""
from math import gcd
N = int(input())
ats = 0
i = 1
while i * i <= N:
    if N % i == 0:
        if i != 1:
            ats = gcd(ats, i)
        ats = gcd(ats, N // i)
    i += 1
print(ats)
