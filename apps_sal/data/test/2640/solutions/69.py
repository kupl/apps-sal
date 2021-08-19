import numpy as np


def lamp(s):
    h = len(s)
    w = s.size // h
    A = np.zeros((h, w), np.int64)
    for i in range(1, w):
        A[:, i] = np.where(s[:, i - 1] == '.', A[:, i - 1] + 1, 0)
    return A


(H, W) = map(int, input().split())
S = np.array([[*input()] for _ in range(H)])
L = lamp(S)
R = lamp(S[:, ::-1])[:, ::-1]
U = lamp(S.T).T
D = lamp(S.T[:, ::-1])[:, ::-1].T
LRUD = L + R + U + D
print(LRUD[S == '.'].max().max() + 1)
