from math import gcd
n, k = list(map(int, input().split()))
print(10 ** k * n // gcd(10 ** k, n))
