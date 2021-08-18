import sys
from fractions import gcd
input = sys.stdin.readline

t = int(input())
for i in range(t):
    r, b, k = [int(item) for item in input().split()]
    if r > b:
        r, b = b, r
    g = gcd(r, b)
    maxima = (b - g + r - 1) // r
    if maxima >= k:
        print("REBEL")
    else:
        print("OBEY")
