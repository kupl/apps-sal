from fractions import gcd
n, m, z = list(map(int, input().split()))
l = n * m / gcd(n, m)
print(int(z // l))
