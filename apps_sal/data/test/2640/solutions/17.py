import sys
import numpy as np
sys.setrecursionlimit(10**9)
H, W = list(map(int, input().split()))
S = [list('
for _ in range(H):
    S.append(list('
S.append(list('
S=np.array(S)

north=np.zeros_like(S, dtype='int')
for w in range(1, W + 1):
    north[:, w]=north[:, w - 1] + 1
    north[:, w][S[:, w - 1] == '
    north[:, w][S[:, w] == '

south=np.zeros_like(S, dtype='int')
for w in range(W, 0, -1):
    south[:, w]=south[:, w + 1] + 1
    south[:, w][S[:, w + 1] == '
    south[:, w][S[:, w] == '

east=np.zeros_like(S, dtype='int')
for h in range(1, H + 1):
    east[h, :]=east[h - 1, :] + 1
    east[h, :][S[h - 1] == '
    east[h, :][S[h, :] == '

west=np.zeros_like(S, dtype='int')
for h in range(H, 0, -1):
    west[h, :]=west[h + 1, :] + 1
    west[h, :][S[h + 1] == '
    west[h, :][S[h, :] == '

ans=north + south + east + west
print((ans.max() + 1))
