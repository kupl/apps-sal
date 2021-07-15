# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

H, W = lr()
S = [list(sr()) for _ in range(H)]
up = np.array([[1 if x == '.' else 0 for x in row] for row in S])
down = up.copy()
right = up.copy()
left = up.copy()
S = up.copy()
for i in range(H-1):
    up[i+1] += up[i]
    up[i+1] *= S[i+1]
for i in range(H-1, 0, -1):
    down[i-1] += down[i]
    down[i-1] *= S[i-1]
for i in range(W-1):
    left[:, i+1] += left[:, i]
    left[:, i+1] *= S[:, i+1]
for i in range(W-1, 0, -1):
    right[:, i-1] += right[:, i]
    right[:, i-1] *= S[:, i-1]

answer = (up + down + left + right).max() - 3
print(answer)

