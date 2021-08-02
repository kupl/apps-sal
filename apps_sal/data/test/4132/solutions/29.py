from math import *
n = int(input())
a = sorted(map(int, input().split()))
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
print(g)
