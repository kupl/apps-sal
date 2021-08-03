import numpy as np
N, K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
A = np.array(A, dtype="int64")
Z = A[A == 0]
H = A[A < 0]
S = A[A > 0]
l, r = -10**19, 10**19
while r - l > 1:
    mid = (r + l) // 2
    cnt = 0
    cnt += A.searchsorted(mid // S, side="right").sum()
    cnt += (N - A.searchsorted((-mid - 1) // (-H), side="right")).sum()
    cnt -= np.count_nonzero(A * A <= mid)
    if mid >= 0:
        cnt += len(Z) * N
    cnt //= 2
    if cnt >= K:
        r = mid
    else:
        l = mid
print(r)
