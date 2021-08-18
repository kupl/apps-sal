N, W = map(int, input().split())
wv = [list(map(int, input().split())) for i in range(N)]
w1 = wv[0][0]

w_to_idx = {0: 0}
idx_to_w = {0: 0}
idx_W = 0


def calc():
    nonlocal w_to_idx, idx_to_w, idx_W
    idx = 1
    w_max = 0
    for i in range(1, N + 1):
        w = w1 * i
        for j in range(3 * i + 1):
            ww = w + j
            if ww in w_to_idx:
                continue
            w_to_idx[ww] = idx
            idx_to_w[idx] = ww
            if w_max < ww <= W:
                w_max = ww
                idx_W = idx
            idx += 1


calc()
n = len(w_to_idx)
dp = [[0] * n for i in range(N + 1)]
for i, (w, v) in enumerate(wv, 1):
    for j in range(n):
        dp[i][j] = dp[i - 1][j]
        ww = idx_to_w[j]
        if ww >= w and ww - w in w_to_idx:
            jj = w_to_idx[ww - w]
            dp[i][j] = max(dp[i][j], dp[i - 1][jj] + v)

print(max(dp[-1][:idx_W + 1]))
