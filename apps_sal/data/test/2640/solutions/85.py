import numpy as np

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
S = np.array(S)
S = (S == '.') * 1

R = np.zeros((H, W), dtype=int)
L = np.zeros((H, W), dtype=int)
U = np.zeros((H, W), dtype=int)
D = np.zeros((H, W), dtype=int)

for i in range(W):
    if i == 0:
        L[:, 0] = S[:, 0]
        R[:, W - 1] = S[:, W - 1]
    else:
        L[:, i] = L[:, i - 1] * S[:, i] + S[:, i]
        R[:, W - i - 1] = R[:, W - i] * S[:, W - i - 1] + S[:, W - i - 1]
for i in range(H):
    if i == 0:
        U[i] = S[i]
        D[H - 1] = S[H - 1]
    else:
        U[i] = U[i - 1] * S[i] + S[i]
        D[H - i - 1] = D[H - i] * S[H - i - 1] + S[H - i - 1]

print(np.max(R + L + U + D) - 3)
