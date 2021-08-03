import numpy as np

N, M = map(int, input().split())
A = np.array(input().split(), np.int64)

A = np.sort(A)
S = np.zeros(N + 1, np.int64)
S[1:] = np.cumsum(A)

hi = 200001
lo = -1

while hi - lo > 1:
    mid = (hi + lo) // 2
    above_mid = (N - np.searchsorted(A, mid - A, side='left')).sum()
    if above_mid >= M:
        lo = mid
    else:
        hi = mid

X = np.searchsorted(A, hi - A, side='left')

above_hi = (N - X).sum()
happiness = (S[-1] - S[X]).sum()
happiness += (A * (N - X)).sum()
happiness += (M - above_hi) * lo

print(happiness)
