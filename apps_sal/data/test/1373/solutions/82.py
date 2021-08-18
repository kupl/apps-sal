import numpy as np

N, K = map(int, input().split())


A = [i for i in range(N + 1)]
A = np.array(A)
cum_A = np.cumsum(A)

cnt = 0
for i in range(K, N + 1):
    cnt += (cum_A[N] - cum_A[N - i]) - cum_A[i - 1] + 1
print((cnt + 1) % (10**9 + 7))
