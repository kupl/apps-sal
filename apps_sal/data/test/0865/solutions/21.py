import numpy as np
N, T = map(int, input().split())

menu = []
for _ in range(N):
    m = tuple(map(int, input().split()))
    menu.append(m)
menu = sorted(menu, key=lambda m: m[0])

# 料理i-1をj-1分までに完食するときの満足度最大値
dp = np.zeros((N, T), dtype='int64')
anss = []

for i in range(1, N):
    # 一つまえのメニューについて
    ai, bi = menu[i-1]
    dp[i][:ai] = dp[i-1][:ai]  # 時間が足りないので注文しない
    dp[i][ai:] = np.fmax(
        dp[i-1][ai:], # 何も注文しない
        dp[i-1][:-ai] + bi # 注文した場合, ai分かかっても大丈夫な範囲から取得
    )
    # 加えて自身を最後に食べた場合を記録
    anss.append(dp[i][-1] + menu[i][1])

print(max(anss))
