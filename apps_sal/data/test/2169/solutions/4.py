import sys

import numba as nb
import numpy as np

input = sys.stdin.readline


@nb.njit("void(i8,i8,i8,i8[:,:],i8,i8[:,:],i8[:])", cache=True)
def dfs(H, W, D, A, Q, LR, ans):
    position = [(-1, -1)] * (H * W + 1)
    for h in range(H):
        for w in range(W):
            position[A[h][w]] = (h, w)

    mp = np.zeros(shape=(H * W + 1), dtype=np.int64)

    for i in range(1, H * W + 1 - D):
        h, w = position[i]
        y, x = position[i + D]
        mp[i + D] = abs(x - w) + abs(y - h)

    for d in range(1, D + 1):
        mp[d::D] = np.cumsum(mp[d::D])

    for i in range(Q):
        l, r = LR[i]
        ans[i] = mp[r] - mp[l]


def main():
    H, W, D = list(map(int, input().split()))
    A = np.zeros(shape=(H, W), dtype=np.int64)
    for i in range(H):
        A[i] = tuple(map(int, input().split()))
    Q = int(input())
    LR = np.zeros(shape=(Q, 2), dtype=np.int64)
    for i in range(Q):
        LR[i] = tuple(map(int, input().split()))

    ans = np.zeros(shape=Q, dtype=np.int64)
    dfs(H, W, D, A, Q, LR, ans)

    print(("\n".join(map(str, ans))))


def __starting_point():
    main()


__starting_point()
