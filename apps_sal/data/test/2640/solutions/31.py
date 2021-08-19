import numpy as np

H, W = map(int, input().split())
S_list = [list(input()) for _ in range(H)]
S_list = (np.array(S_list) == ".") * 1

L = np.zeros((H, W), int)  # i,jより左のランプをてらせる数
R = np.zeros((H, W), int)
U = np.zeros((H, W), int)
D = np.zeros((H, W), int)

for w in range(W):
    if w == 0:
        L[:, w] = S_list[:, w]  # 一番左であれば、Lは1, 他の行も同じ
        R[:, W - w - 1] = S_list[:, W - w - 1]  # 一番右であれば、Rは1, 他の行も同じ
    else:
        L[:, w] = (L[:, w - 1] + 1) * S_list[:, w]  # Lは一つ左のものに1を加えたもの, 他の行も同じ
        R[:, W - w - 1] = (R[:, W - w] + 1) * S_list[:, W - w - 1]  # Rは一つ右のものに1を加えたもの, 他の行も同じ

for h in range(H):
    if h == 0:
        U[h, :] = S_list[h, :]
        D[H - h - 1, :] = S_list[H - h - 1, :]
    else:
        U[h, :] = (U[h - 1, :] + 1) * S_list[h, :]
        D[H - h - 1, :] = (D[H - h, :] + 1) * S_list[H - h - 1, :]

ans = max(np.max(L + R + U + D - 3), 0)  # 行列のH,Wの中で最大のものをとる

print(ans)
