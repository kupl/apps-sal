import numpy as np

N, K = map(int, input().split())
A = list(map(int, input().split()))


A = np.array(A)
cum_A = np.cumsum(A)
cum_A = np.insert(cum_A, 0, 0)


cnt = 0
j = 1
for i in range(1, N + 1):
    while(j <= N):
        if cum_A[j] - cum_A[i - 1] >= K:
            cnt += N - j + 1
            break
        j += 1
print(cnt)
