(N, M) = map(int, input().split())
st = [list(map(int, input().split())) for i in range(M)]
way = [[] for i in range(N)]
for (s, t) in st:
    way[s - 1].append(t - 1)
dp = [0] * N
dp_reducable = [0] * N
pr = [0] * N
pr[0] = 1
for i in range(N - 1, -1, -1):
    l = len(way[i])
    if l > 1:
        MAX = 0
        x = 0
        for j in way[i]:
            x += dp[j]
            if dp[j] > MAX:
                MAX = dp[j]
        x_r = (x - MAX) / (l - 1) + 1
        x = x / l + 1
        x_r = x - x_r
    elif l == 0:
        continue
    else:
        x = dp[way[i][0]] + 1
        x_r = 0
    dp[i] = x
    dp_reducable[i] = x_r
    i = N - 1 - i - 1
    l = len(way[i])
    for j in way[i]:
        pr[j] += pr[i] / l
print(dp[0] - max((p * r for (p, r) in zip(pr, dp_reducable))))
