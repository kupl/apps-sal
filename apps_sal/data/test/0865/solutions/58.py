import numpy as np
(N, T) = map(int, input().split())
A = []
B = []
for i in range(N):
    (a, b) = map(int, input().split())
    A.append(a)
    B.append(b)
A = np.array(A, np.int)
B = np.array(B, np.int)
idx = np.argsort(A)
A = A[idx]
B = B[idx]
dp = np.zeros((N, T), np.int)
for i in range(N - 1):
    dp[i + 1, :A[i]] = dp[i, :A[i]]
    dp[i + 1, A[i]:] = np.maximum(dp[i, A[i]:], dp[i, :-A[i]] + B[i])
print(np.max(dp[:, -1] + B))
