from math import gcd
n = int(input())
l = 1
for i in range(1, n + 1):
    l = (l * i) // gcd(l, i)

print((l + 1))
