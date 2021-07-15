import numpy as np
N = int(input())
A = np.array([input().split() for _ in range(N)], dtype=np.int64)

np.fill_diagonal(A, 10**9)

ans = 0
for i in range(N):
  for j in range(i+1,N):
    d = np.min(A[i]+A[j])
    if A[i][j] < d:
      ans += A[i][j]
    elif d < A[i][j]:
      print((-1))
      return

print(ans)

