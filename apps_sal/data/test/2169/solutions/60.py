import sys
import math
import collections
import itertools
input = sys.stdin.readline
(H, W, D) = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(H)]
Q = int(input())
LR = [list(map(int, input().split())) for i in range(Q)]
dict_map = {}
for ih in range(H):
    for iw in range(W):
        dict_map[A[ih][iw]] = (ih, iw)
memo = [-1] * (H * W + 1)
for i in range(1, D + 1):
    useMP = 0
    direct = list(range(i, H * W + 1, D))
    memo[i] = 0
    for p in range(len(direct) - 1):
        (x0, y0) = dict_map[direct[p]]
        (x1, y1) = dict_map[direct[p + 1]]
        dist = abs(x0 - x1) + abs(y0 - y1)
        useMP += dist
        memo[direct[p + 1]] = useMP
for q in range(Q):
    (L, R) = LR[q]
    print(memo[R] - memo[L])
