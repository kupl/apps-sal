import copy

N, Ma, Mb = list(map(int, input().split()))
ABC = [tuple(map(int, input().split())) for _ in range(N)]

INF, W = 10000, 10 * max(Ma, Mb) * N
dp = [[INF] * (2 * W + 1)]

for a, b, c in ABC:
    dp.append(copy.deepcopy(dp[-1]))
    df = a * Mb - b * Ma
    dp[-1][df] = min(dp[-1][df], c)
    for d in range(-W, W + 1):
        dp[-1][df + d] = min(dp[-1][df + d], c + dp[-2][d])

print(("-1" if dp[N][0] == INF else dp[N][0]))
