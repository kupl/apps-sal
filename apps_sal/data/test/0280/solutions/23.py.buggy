# C - Camels and Bridge
import itertools
import bisect

n, m = map(int, input().split())
w = tuple(map(int, input().split()))
lv = []
for i in range(m):
    l, v = map(int, input().split())
    lv.append([v, l])

lv.sort(key=lambda x: (x[0], -x[1]))
# print(lv)
for wi in w:
    if wi > lv[0][0]:
        print(-1)
        return
mx = 0
# より耐荷重が小さいパーツの長さが優先される。
# 耐荷重4長さ10と耐荷重7長さ5のパーツがあったら、後者のパーツは無視される。
# (重量7でも10の間隔が必要)
for i in range(m):
    mx = max(lv[i][1], mx)
    lv[i][1] = mx
# lv.append([float('inf'),lv[-1][1]])
lv = [[0, 0]] + lv

b = {}


def f(x):
    if x in b:
        return b[x]
    else:
        b[x] = bisect.bisect_left(lv, [x, 0])
        return b[x]


ans = float('inf')
# ラクダのすべての並び順を全探索する。
for p in itertools.permutations(range(n)):
    # dp[i][j]:とらなければいけないi番目のラクダからj番目のラクダまで間隔の最小値
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            ww = 0
            for k in range(i, j + 1):
                ww += w[p[k]]
            # idx = bisect.bisect_left(lv,[ww,0])
            idx = f(ww)
            # print(ww,idx,lv)
            dp[i][j] = lv[idx - 1][1]
    # 例えば0,j,i番目のラクダについて考えると、0とiの間隔は
    # dp[0][i]とdp[0][j]+dp[j][i]の長い方にする必要がある。
    for i in range(1, n):
        for j in range(i):
            dp[0][i] = max(dp[0][j] + dp[j][i], dp[0][i])
    ans = min(dp[0][n - 1], ans)
print(ans)
