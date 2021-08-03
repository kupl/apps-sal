"""This code was written by
Russell Emerine - linguist,
mathematician, coder,
musician, and metalhead."""
from math import gcd
n = int(input())
for _ in range(n):
    r, b, k = list(map(int, input().split()))
    g = gcd(r, b)
    r //= g
    b //= g
    if (r + b - 2) // b >= k:
        print("REBEL")
    elif (b + r - 2) // r >= k:
        print("REBEL")
    else:
        print("OBEY")
