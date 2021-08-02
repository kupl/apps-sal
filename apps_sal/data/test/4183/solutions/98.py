from math import gcd
n = int(input())
a = 1
for _ in range(n):
    x = int(input())
    a = a // gcd(a, x) * x
print(a)
