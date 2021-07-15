from math import gcd

n, k = list(map(int , input().split()))
l = n * (10 ** k)
g = gcd(n, 10 ** k)
print(l // g)
