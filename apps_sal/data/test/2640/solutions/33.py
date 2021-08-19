# coding: utf-8
import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


H, W = lr()

S = [list(sr()) for _ in range(H)]
S = np.array([[1 if x == '.' else 0 for x in row] for row in S])

U = np.zeros((H, W), np.int32)
D = np.zeros((H, W), np.int32)
L = np.zeros((H, W), np.int32)
R = np.zeros((H, W), np.int32)

for h in range(H - 1):
    U[h + 1] = (U[h] + 1) * S[h]
    D[H - h - 2] = (D[H - h - 1] + 1) * S[H - h - 1]
for w in range(W - 1):
    L[:, w + 1] = (L[:, w] + 1) * S[:, w]
    R[:, W - w - 2] = (R[:, W - w - 1] + 1) * S[:, W - w - 1]


print((((U + D + L + R) * S).max() + 1))
