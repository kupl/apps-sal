from math import*
N = int(input())
*A, = map(int, input().split())
R = [0] * (N + 1)
for i in range(N):
    R[-i - 2] = gcd(R[-i - 1], A[-i - 1])
L = 0
M = 1
for i in range(N):
    M = max(M, (gcd(L, R[i + 1])))
    L = gcd(L, A[i])
print(M)
