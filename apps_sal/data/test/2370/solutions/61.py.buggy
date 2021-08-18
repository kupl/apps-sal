from numpy import *
N = int(input())
A = array([input().split() for _ in range(N)], dtype=int64)

fill_diagonal(A, 10**9)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        d = min(A[i] + A[j])
        if A[i][j] < d:
            ans += A[i][j]
        elif d < A[i][j]:
            print((-1))
            return

print(ans)
