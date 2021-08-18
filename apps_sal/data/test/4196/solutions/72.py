from math import gcd

N = int(input())
A = list(map(int, input().split()))

A = [0] + A + [0]

L = [A[1]]
tempL = A[1]
for i in range(1, N):
    tempL = gcd(tempL, A[i + 1])
    L.append(tempL)
L = [0] + L

R = [A[-2]]
tempR = A[-2]
for i in range(1, N):
    tempR = gcd(tempR, A[-i - 2])
    R.append(tempR)
R = list(reversed(R)) + [0]

ans = []
for i in range(N):
    result = gcd(L[i], R[i + 1])
    ans.append(result)

print((max(ans)))
