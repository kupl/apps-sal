(N, Ma, Mb) = map(int, input().split())
ABC = [tuple(map(int, input().split())) for _ in range(N)]
INF = float('inf')
DP = [[[INF] * (11 * N + 1) for _ in range(11 * N + 1)] for _ in range(N + 1)]
DP[0][0][0] = 0
for (i, (a, b, c)) in enumerate(ABC):
    for j in range(10 * N + 1):
        for k in range(10 * N + 1):
            if DP[i][j][k] == INF:
                continue
            DP[i + 1][j][k] = min(DP[i + 1][j][k], DP[i][j][k])
            DP[i + 1][j + a][k + b] = min(DP[i + 1][j + a][k + b], DP[i][j][k] + c)
ans = INF
for j in range(1, 10 * N + 1):
    for k in range(1, 10 * N + 1):
        if Ma * k == Mb * j:
            ans = min(ans, DP[N][j][k])
if ans == INF:
    ans = -1
print(ans)
