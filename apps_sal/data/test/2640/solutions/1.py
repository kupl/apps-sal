# numpy使い、ループが2→１にする
import numpy as np
# 初期入力
H, W = (int(x) for x in input().split())
map1 = [list(input()) for i in range(H)]
map_np = (np.array(map1) == ".") * 1

L = np.zeros((H, W), dtype=int)
R = np.zeros((H, W), dtype=int)
U = np.zeros((H, W), dtype=int)
D = np.zeros((H, W), dtype=int)

L[:, 0] = map_np[:, 0]
for i in range(1, W):  # if map_np[i,j] ==1: ⇒ *map_npで１or０をかけてるから不要
    L[:, i] = (L[:, i - 1] + 1) * map_np[:, i]

R[:, W - 1] = map_np[:, W - 1]
for i in range(W - 1 - 1, -1, -1):
    R[:, i] = (R[:, i + 1] + 1) * map_np[:, i]

U[0, :] = map_np[0, :]
for i in range(1, H):
    U[i, :] = (U[i - 1, :] + 1) * map_np[i, :]

D[H - 1, :] = map_np[H - 1, :]
for i in range(H - 1 - 1, -1, -1):
    D[i, :] = (D[i + 1, :] + 1) * map_np[i, :]

ans = L + R + U + D - 3
print(np.max(ans))
