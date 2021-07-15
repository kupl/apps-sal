from fractions import gcd
n, m, z = list(map(int, input().split()))
print(z // ((n * m) // gcd(n, m)))

