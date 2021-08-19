# coding: utf-8
import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


H, W = lr()
S = np.array(['#' * (W + 2)] + ['#' + sr() + '#' for _ in range(H)] + ['#' * (W + 2)])
S = np.array([[x == '.' for x in row] for row in S])
S = S.astype(np.int16)
left = S.copy()
right = S.copy()
up = S.copy()
down = S.copy()
for i in range(1, W + 1):
    left[:, i] += left[:, i - 1]
    left[:, i] *= S[:, i]
for i in range(W, 0, -1):
    right[:, i] += right[:, i + 1]
    right[:, i] *= S[:, i]
for i in range(1, H + 1):
    up[i, :] += up[i - 1, :]
    up[i, :] *= S[i, :]
for i in range(H, 0, -1):
    down[i, :] += down[i + 1, :]
    down[i, :] *= S[i, :]

answer = (left + right + up + down - 3).max()
print(answer)
