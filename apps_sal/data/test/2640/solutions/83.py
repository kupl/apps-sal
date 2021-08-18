import numpy as np

H, W = map(int, input().split())
S = []
for h in range(H):
    S.append(list(input()))
G = np.array(S)
G = np.where(G == ".", 1, 0)

L = np.zeros((H, W), dtype=int)
R = np.zeros((H, W), dtype=int)
U = np.zeros((H, W), dtype=int)
D = np.zeros((H, W), dtype=int)

for w in range(1, W):
    L[:, w] = (L[:, w - 1] + 1) * (G[:, w - 1])
for w in range(W - 1, 0, -1):
    R[:, w - 1] = (R[:, w] + 1) * (G[:, w])
for h in range(1, H):
    U[h] = (U[h - 1] + 1) * (G[h - 1])
for h in range(H - 1, 0, -1):
    D[h - 1] = (D[h] + 1) * (G[h])

ans = np.max((L + R + U + D) * G) + 1
print(ans)
