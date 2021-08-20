import numpy as np
(N, T) = map(int, input().split())
A = []
B = []
for _ in range(N):
    (A_temp, B_temp) = map(int, input().split())
    A.append(A_temp)
    B.append(B_temp)
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
