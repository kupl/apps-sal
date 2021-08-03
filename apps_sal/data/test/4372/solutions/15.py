from math import gcd
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

x = max(A)


z = 0
SUM = 0
for a in A:
    z = gcd(z, x - a)
    SUM += x - a

y = SUM // z

print(y, z)
