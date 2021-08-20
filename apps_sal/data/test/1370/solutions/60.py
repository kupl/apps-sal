import sys


def da_generate(h, w, a):
    da = [[0] * w for j in range(h)]
    da[0][0] = a[0][0]
    for i in range(1, w):
        da[0][i] = da[0][i - 1] + a[0][i]
    for i in range(1, h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i - 1][j] + cnt_w
    return da


def da_calc(p, q, x, y):
    if p > x or q > y:
        return 0
    if p == 0 and q == 0:
        return da[x][y]
    if p == 0:
        return da[x][y] - da[x][q - 1]
    if q == 0:
        return da[x][y] - da[p - 1][y]
    return da[x][y] - da[p - 1][y] - da[x][q - 1] + da[p - 1][q - 1]


(H, W, K) = map(int, sys.stdin.readline().rstrip().split())
grid = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(H)]
da = da_generate(H, W, grid)
ans = 10 ** 18
for i in range(2 ** (H - 1)):
    res = 0
    s = [k for (k, j) in enumerate(range(H), 1) if i >> j & 1]
    res += len(s)
    s.append(H)
    y = 0
    for w in range(1, W + 1):
        x = 0
        flag = False
        for s_i in s:
            if da_calc(x, y, s_i - 1, w - 1) > K:
                if y + 1 < w:
                    res += 1
                    y = w - 1
                else:
                    flag = True
                break
            x = s_i
        else:
            pass
        if flag:
            break
    else:
        ans = min(ans, res)
print(ans)
