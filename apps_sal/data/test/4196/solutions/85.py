from math import *
N = int(input())
(*A,) = map(int, input().split())
R = [0]
r = A[-1]
for a in A[::-1]:
    r = gcd(a, r)
    R.append(r)
R = R[::-1]
M = []
L = 0
for i in range(N):
    M.append(gcd(L, R[i + 1]))
    L = gcd(L, A[i])
print(max(M))
