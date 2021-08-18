from numpy import *
N = int(input())
A = array([list(map(int, input().split())) for n in range(N)])

fill_diagonal(A, 10**10)

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
