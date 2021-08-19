import sys
from math import gcd
N = int(input())
A = list(map(int, input().split()))
L = [0]
R = [0]
for i in range(N):
    L.append(gcd(L[-1], A[i]))
for i in range(N)[::-1]:
    R.append(gcd(R[-1], A[i]))
R.reverse()
M = 0
for i in range(N):
    M = max(M, gcd(L[i], R[i + 1]))
print(M)
