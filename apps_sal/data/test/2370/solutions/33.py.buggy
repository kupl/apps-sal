from numpy import *
N = int(input())
A = array([list(map(int, input().split())) for n in range(N)])
ans = 0

for n in range(N):
    A[n][n] = 10**9

for i in range(N):
    for j in range(i + 1, N):
        dp = min(A[i] + A[j])
        if A[i][j] < dp:
            ans += A[i][j]
        elif dp < A[i][j]:
            print(-1)
            return

print(ans)
