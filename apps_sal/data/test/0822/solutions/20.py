from fractions import gcd

from sys import stdin as fin
# fin = open("cfr395a.in", "r")

n, m, z = map(int, fin.readline().split())
# n = int(fin.readline())
print(z // (n * m // gcd(n, m)))
