import numpy as np

H, W = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]
S = np.array(S) == "."

L = np.zeros((H, W), dtype=int)
R = np.zeros((H, W), dtype=int)
U = np.zeros((H, W), dtype=int)
D = np.zeros((H, W), dtype=int)

for i in range(H):
    D[i] = (D[i-1]+1) * S[i]
    U[-i-1] = (U[-i]+1) * S[-i-1]

for i in range(W):
    R[:, i] = (R[:, i-1]+1) * S[:, i]
    L[:, -i-1] = (L[:, -i]+1) * S[:, -i-1]

print((np.max(L+R+U+D)-3))

