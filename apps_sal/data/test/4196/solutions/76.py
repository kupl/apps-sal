import math
N = int(input())
A = list(map(int, input().split()))

L = [0] * (N + 1)
R = [0] * (N + 1)

for i in range(N):
    L[i + 1] = math.gcd(L[i], A[i])
    R[N - i - 1] = math.gcd(R[N - i], A[N - i - 1])

ans = 0
for i in range(N):
    ans = max(ans, math.gcd(L[i], R[i + 1]))

print(ans)
