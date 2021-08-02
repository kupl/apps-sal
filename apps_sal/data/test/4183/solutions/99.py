from math import gcd

n = int(input())
g = int(input())

for i in range(n - 1):
    t = int(input())
    g = g * t // gcd(g, t)

print(g)
