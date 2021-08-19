import numpy as np
import sys
input = sys.stdin.readline
(N, M, Q) = map(int, input().split())
T = np.zeros((N, N), dtype=np.int32)
for _ in [0] * M:
    (l, r) = map(int, input().split())
    T[l - 1, r - 1] += 1
T = T[::-1].cumsum(axis=0).cumsum(axis=1)[::-1]
for _ in [0] * Q:
    (p, q) = map(int, input().split())
    print(T[p - 1, q - 1])
