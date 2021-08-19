from math import gcd
n = int(input())
l = list(map(int, input().split()))
GCD = l[0]
for i in range(1, n):
    GCD = gcd(GCD, l[i])
print(GCD)
