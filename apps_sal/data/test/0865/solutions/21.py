import numpy as np
N, T = map(int, input().split())

menu = []
for _ in range(N):
    m = tuple(map(int, input().split()))
    menu.append(m)
menu = sorted(menu, key=lambda m: m[0])

dp = np.zeros((N, T), dtype='int64')
anss = []

for i in range(1, N):
    ai, bi = menu[i - 1]
    dp[i][:ai] = dp[i - 1][:ai]
    dp[i][ai:] = np.fmax(
        dp[i - 1][ai:],
        dp[i - 1][:-ai] + bi
    )
    anss.append(dp[i][-1] + menu[i][1])

print(max(anss))
