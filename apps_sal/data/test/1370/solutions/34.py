# coding: utf-8
import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


H, W, K = lr()
S = np.array([list(map(int, sr())) for _ in range(H)])
Scum = np.cumsum(S, axis=1)
INF = 10 ** 10
answer = INF
for pattern in range(1 << H - 1):
    cnt = 0
    Tcum = Scum.copy()
    for i in range(H - 1):
        if pattern >> i & 1:  # 切れ目
            cnt += 1
        else:
            Tcum[i + 1] += Tcum[i]
    prev = -1
    w = 0
    Tcum = Tcum.tolist()
    while w < W:
        cut = False
        for i in range(H):
            if Tcum[i][w] - (Tcum[i][prev] if prev >= 0 else 0) > K:
                cut = True
                break
        if cut:
            if prev == w - 1:  # 1列でKをオーバー
                break
            cnt += 1
            prev = w - 1
        else:
            w += 1
    else:
        answer = min(answer, cnt)

print(answer)
