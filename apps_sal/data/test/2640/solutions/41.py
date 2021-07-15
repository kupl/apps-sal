# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

H, W = lr()
S = [list(sr()) for _ in range(H)]
S = np.array([[1 if x == '.' else 0 for x in row] for row in S], np.bool)
up = np.zeros((H, W), np.int32)
down = np.zeros((H, W), np.int32)
right = np.zeros((H, W), np.int32)
left = np.zeros((H, W), np.int32)
for i in range(H-1):
    up[i+1] = (1+up[i]) * S[i]
for i in range(H-1, 0, -1):
    down[i-1] = (1+down[i]) * S[i]
for i in range(W-1):
    left[:, i+1] = (1+left[:, i]) * S[:, i]
for i in range(W-1, 0, -1):
    right[:, i-1] = (1+right[:, i]) * S[:, i]

answer = ((up + down + left + right) * S).max() + 1
print(answer)

