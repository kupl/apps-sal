import sys
from itertools import product
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (H, W, K) = list(map(int, input().split()))
    grid = [list(input()) for _ in range(H)]
    R = [[0] * (W + 1) for _ in range(H + 1)]
    for h in range(H):
        for w in range(W):
            R[h + 1][w + 1] = R[h][w + 1] + R[h + 1][w] - R[h][w] + int(grid[h][w])
    res = f_inf
    for pattern in product([0, 1], repeat=H - 1):
        cut_H = [idx + 1 for (idx, p) in enumerate(pattern) if p == 1] + [H]
        cnt_cut = sum(pattern)
        left = 0
        right = 1
        flg = 1
        while right <= W:
            if not flg:
                break
            up = 0
            for bottom in cut_H:
                cnt_w = R[bottom][right] - R[bottom][left] - R[up][right] + R[up][left]
                if cnt_w > K:
                    if right - left == 1:
                        flg = False
                    cnt_cut += 1
                    left = right - 1
                    break
                else:
                    up = bottom
            else:
                right += 1
        else:
            res = min(res, cnt_cut)
    print(res)


def __starting_point():
    resolve()


__starting_point()
