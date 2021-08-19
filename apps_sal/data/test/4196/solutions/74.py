import math
N = int(input())
A = list(map(int, input().split()))
A = [0] + A
L = [0 for i in range(N + 2)]
R = [0 for i in range(N + 2)]
for i in range(0, N + 1):
    L[i + 1] = math.gcd(L[i], A[i])
for i in range(N, -1, -1):
    R[i] = math.gcd(R[i + 1], A[i])
M = [0 for i in range(N + 1)]
for i in range(1, N + 1):
    M[i] = math.gcd(L[i], R[i + 1])
print(max(M))
