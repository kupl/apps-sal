import numpy as np
H, W = (int(x) for x in input().split())
S = [list(input()) for i in range(H)]
S_np = (np.array(S) == ".") * 1


L = np.zeros((H, W), dtype=int)
R = np.zeros((H, W), dtype=int)
U = np.zeros((H, W), dtype=int)
D = np.zeros((H, W), dtype=int)
for i in range(W):
    if i == 0:
        L[:, i] = S_np[:, i]
        R[:, W - i - 1] = S_np[:, W - i - 1]
    else:
        L[:, i] = (L[:, i - 1] + 1) * S_np[:, i]
        R[:, W - i - 1] = (R[:, W - i] + 1) * S_np[:, W - i - 1]

for i in range(H):
    if i == 0:
        D[i, :] = S_np[i, :]
        U[H - i - 1, :] = S_np[H - i - 1, :]
    else:
        D[i, :] = (D[i - 1, :] + 1) * S_np[i, :]
        U[H - i - 1, :] = (U[H - i, :] + 1) * S_np[H - i - 1, :]

light = L + R + D + U - 3
light_max = np.max(light)
print(light_max)
