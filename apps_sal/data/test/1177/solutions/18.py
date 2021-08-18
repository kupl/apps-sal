import numpy as np
N, S = list(map(int, input().split()))
A = [0] + list(map(int, input().split()))

dt = np.array([[0 for _ in range(S + 1)] for x in range(N + 1)])

for n in range(1, N + 1):
    if A[n] <= S:
        dt[n, A[n]] += n
    if A[n] < S:
        dt[n, A[n] + 1:] += dt[n - 1, 1:S - A[n] + 1] - dt[n - 2, 1:S - A[n] + 1]
    dt[n, :] += dt[n - 1, :] * 2 - dt[n - 2, :]
    dt[n, :] %= 998244353
print(dt[N, S] % 998244353)
