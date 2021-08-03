# E - Dividing Chocolate
import numpy as np

H, W, K = list(map(int, input().split()))
S = np.zeros((H, W), dtype=np.int64)

ans = H + W

for i in range(H):
    S[i] = list(str(input()))

for m in range(2**(H - 1)):
    wp = np.zeros((H, W), dtype=np.int64)
    wq = np.zeros((H, ), dtype=np.int64)
    wp[0] = S[0]
    cut = 0
    for n in range(H - 1):
        if m >> n & 1:
            cut += 1
        wp[cut] += S[n + 1]

    if cut >= ans or np.count_nonzero(wp > K):
        continue

    for j in range(W):
        wq += wp[:, j]
        if np.count_nonzero(wq > K):
            cut += 1
            wq = wp[:, j]
    ans = min(ans, cut)

print(ans)
