import numpy as np
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]
d = []
for i in range(h):
    d.append([abs(a[i][j] - b[i][j]) for j in range(w)])
dp = np.zeros((h, w, 12800))
# dp[r][c][j]:(r,c)まで考えたときjにできるか。0：できない。1以上：できる。
dp[0, 0, d[0][0] + 6400] = 1
for i in range(w - 1):
    if d[0][i + 1] == 0:
        dp[0, i + 1] += dp[0, i]
        continue
    dp[0, i + 1, d[0][i + 1]:] += dp[0, i, :-d[0][i + 1]]
    dp[0, i + 1, :-d[0][i + 1]] += dp[0, i, d[0][i + 1]:]
for i in range(h - 1):
    if d[i + 1][0] == 0:
        dp[i + 1, 0] += dp[i, 0]
        continue
    dp[i + 1, 0, d[i + 1][0]:] += dp[i, 0, :-d[i + 1][0]]
    dp[i + 1, 0, :-d[i + 1][0]] += dp[i, 0, d[i + 1][0]:]
for r in range(1, h):
    for c in range(1, w):
        if d[r][c] == 0:
            dp[r, c] += dp[r - 1, c]
            dp[r, c] += dp[r, c - 1]
            continue
        dp[r, c, d[r][c]:] += dp[r - 1, c, :-d[r][c]]
        dp[r, c, :-d[r][c]] += dp[r - 1, c, d[r][c]:]
        dp[r, c, d[r][c]:] += dp[r, c - 1, :-d[r][c]]
        dp[r, c, :-d[r][c]] += dp[r, c - 1, d[r][c]:]
print(min([abs(e - 6400) for e in np.where(dp[h - 1, w - 1] > 0)[0]]))
