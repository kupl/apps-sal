import numpy as np
N = int(input())
A = np.array([list(map(int, input().split())) for _ in range(N)])

for i in range(N):
    A[i][i] = 10 ** 9

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        dp = np.min(A[i] + A[j])
        if A[i][j] < dp:
            ans += A[i][j]
        elif A[i][j] > dp:
            print((-1))
            return

print(ans)
