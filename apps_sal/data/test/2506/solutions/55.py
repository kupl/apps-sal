import numpy as np
N, M, *A = list(map(int, open(0).read().split()))
A = np.sort(A)
B = np.cumsum(np.concatenate([[0], A[::-1]]))
l = -1
r = 10**6
while l + 1 < r:
    s = (l + r) // 2
    cnt = np.sum(N - np.searchsorted(A, s - A))
    if cnt >= M:
        l = s
    else:
        r = s
ind = np.searchsorted(A, r - A)
M -= np.sum(N - ind)
ans = np.sum(B[N - ind] + A * (N - ind)) + M * l
print(ans)
