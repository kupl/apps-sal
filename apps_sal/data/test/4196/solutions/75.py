from math import *
N = int(input())
(*A,) = map(int, input().split())
L = [0]
l = A[0]
for a in A:
    l = gcd(l, a)
    L.append(l)
R = [0]
r = A[-1]
for a in A[::-1]:
    r = gcd(a, r)
    R.append(r)
R = R[::-1]
M = []
for i in range(N):
    M.append(gcd(L[i], R[i + 1]))
print(max(M))
