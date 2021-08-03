from math import gcd
N = int(input())
A = list(map(int, input().split()))
B = [0 for i in range(N)]
C = [0 for i in range(N)]
B[0] = A[0]
C[0] = A[N - 1]
for i in range(1, N):
    B[i] = gcd(B[i - 1], A[i])
    C[i] = gcd(C[i - 1], A[N - i - 1])


ans = 0
for i in range(N):
    if i != 0 and i != N - 1:
        ans = max(ans, gcd(B[i - 1], C[N - i - 2]))
    elif i == 0:
        ans = max(ans, C[N - 2])
    else:
        ans = max(ans, B[N - 2])

print(ans)
