# coding: utf-8
import math
n = int(input())
A = list(map(int,input().split()))

m = max(A)
m_ = min(A)
g = A[0]
for i in range(n):
    g = math.gcd(g, A[i])

print(g)
