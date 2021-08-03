from math import gcd

A, B = list(map(int, input().split()))

print(A * B // gcd(A, B))
