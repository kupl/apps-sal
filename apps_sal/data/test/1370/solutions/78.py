from itertools import product
import numpy as np
H, W, K = map(int, input().split())

grid = [[] for _ in range(H)]
for i in range(H):
    grid[i] = list(map(int, input()))


def init_cnt():
    _grid = [[0] * W for _ in range(H)]
    _grid[0][0] = grid[0][0]
    for w in range(1, W):
        _grid[0][w] = _grid[0][w - 1] + grid[0][w]
    for h in range(1, H):
        cnt_w = 0
        for w in range(W):
            cnt_w += grid[h][w]
            _grid[h][w] = _grid[h - 1][w] + cnt_w

    return _grid


_grid = init_cnt()


def cnt(x1, x2, y1, y2):
    if x1 == 0 and y1 == 0:
        return _grid[x2][y2]
    if x1 == 0:
        return _grid[x2][y2] - _grid[x2][y1 - 1]
    if y1 == 0:
        return _grid[x2][y2] - _grid[x1 - 1][y2]
    return _grid[x2][y2] - _grid[x2][y1 - 1] - _grid[x1 - 1][y2] + _grid[x1 - 1][y1 - 1]


ans = 1010
for i in range(2 ** (H - 1)):
    res = 0
    lst = list(k for k, j in enumerate(range(H), 1) if i >> j & 1)
    res += len(lst)
    lst.append(H)

    y = 0
    for w in range(1, W + 1):
        x = 0
        flag = False

        for lst_i in lst:
            if cnt(x, lst_i - 1, y, w - 1) > K:
                if y + 1 < w:
                    res += 1
                    y = w - 1
                else:
                    flag = True
                break

            x = lst_i
        else:
            pass
        if flag:
            break
    else:
        ans = min(ans, res)

print(ans)
