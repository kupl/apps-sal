import numpy as np

N = int(input())
A = np.array([input().split() for _ in range(N)], dtype=np.int64).reshape(N,N)

INF = 10**15
np.fill_diagonal(A, INF)

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        detour = np.min(A[i]+A[j])
        if detour > A[i][j]:
            ans+=A[i][j]
        elif detour < A[i][j]:
            print(-1)
            return
print(ans)
