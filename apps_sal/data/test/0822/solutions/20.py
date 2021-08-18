from fractions import gcd

from sys import stdin as fin

n, m, z = map(int, fin.readline().split())
print(z // (n * m // gcd(n, m)))
