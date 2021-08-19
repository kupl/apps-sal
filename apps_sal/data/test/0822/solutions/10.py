from fractions import gcd
(m, n, z) = list(map(int, input().split()))
k = m * n // gcd(m, n)
print(int(z / k))
