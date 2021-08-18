import numpy as np

H, W, K = list(map(int, input().split()))
S = np.zeros((H, W), dtype=np.int64)

ans = H + W

for i in range(H):
    S[i] = list(str(input()))

for m in range(1 << (H - 1)):
    cut = bin(m).count('1')
    if cut >= ans:
        continue

    wp = np.zeros((cut + 1, W), dtype=np.int64)
    wp[0] = S[0]
    c = 0
    for n in range(H - 1):
        if m >> n & 1:
            c += 1
        wp[c] += S[n + 1]

    if np.count_nonzero(wp > K):
        continue

    wq = np.zeros((cut + 1, ), dtype=np.int64)
    for j in range(W):
        wq += wp[:, j]
        if np.count_nonzero(wq > K):
            cut += 1
            wq = wp[:, j]

    ans = min(ans, cut)

print(ans)
