import numpy as np
H, W = list(map(int, input().split()))
S = []
for h in range(H):
    s = list(input())
    S.append(s)
S = np.array(S)
ruit = np.zeros((H, W))
ruit[0, :] = np.where(S[0, :] == ".", 1, 0)
ruil = np.zeros((H, W))
ruil[:, 0] = np.where(S[:, 0] == ".", 1, 0)
ruir = np.zeros((H, W))
ruir[:, -1] = np.where(S[:, -1] == ".", 1, 0)
ruib = np.zeros((H, W))
ruib[-1, :] = np.where(S[-1, :] == ".", 1, 0)

for h in range(1, H):
    nowt = np.where(S[h, :] == ".", 1, 0)
    ruit[h, :] = (ruit[h - 1, :] + nowt) * nowt

    nowb = np.where(S[-(h + 1), :] == ".", 1, 0)
    ruib[-(h + 1), :] = (ruib[-h, :] + nowb) * nowb

for w in range(1, W):
    nowl = np.where(S[:, w] == ".", 1, 0)
    ruil[:, w] = (ruil[:, w - 1] + nowl) * nowl
    nowr = np.where(S[:, -(w + 1)] == ".", 1, 0)
    ruir[:, -(w + 1)] = (ruir[:, -w] + nowr) * nowr
print((int((ruit + ruib + ruil + ruir - 3).max())))
