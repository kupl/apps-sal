(N, Ma, Mb) = map(int, input().split(' '))
med = []
for _ in range(N):
    med.append(tuple(map(int, input().split(' '))))
inf = 10 ** 9 + 7
dp = [[inf for _ in range(401)] for _ in range(401)]
dp[0][0] = 0
for k in range(N):
    (a, b, c) = med[k]
    for i in range(400, -1, -1):
        for j in range(400, -1, -1):
            if dp[i][j] != inf:
                dp[i + a][j + b] = min(dp[i + a][j + b], dp[i][j] + c)
ans = inf
for i in range(401):
    for j in range(401):
        if i == 0 or j == 0:
            continue
        if i * Mb == j * Ma:
            ans = min(ans, dp[i][j])
print(ans if ans != inf else -1)
