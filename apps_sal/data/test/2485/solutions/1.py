#!/usr/bin/env python3
import sys
import numpy as np

input = sys.stdin.readline


def S():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


H, W, M = MI()

R = np.zeros(H + 1)
C = np.zeros(W + 1)
bombs = []
for _ in range(M):
    h, w = MI()
    bombs.append((h, w))
    R[h] += 1
    C[w] += 1

R_max = [R == max(R)]
ans = max(R) + max(C)
C_max = [C == max(C)]

cnt = 0
for h, w in bombs:
    if R_max[0][h] and C_max[0][w]:
        cnt += 1

if cnt == np.count_nonzero(R_max) * np.count_nonzero(C_max):
    print((int(ans - 1)))
else:
    print((int(ans)))

