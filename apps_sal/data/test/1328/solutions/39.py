import copy

N, Ma, Mb = list(map(int, input().split()))
ABC = [tuple(map(int, input().split())) for _ in range(N)]

INF, W = 10 ** 10, N * 10 * max(Ma, Mb)
dp = [[INF] * (W * 2 + 1)]

for a, b, c in ABC:
    dp.append(copy.deepcopy(dp[-1]))
    df = a * Mb - b * Ma
    dp[-1][df + W] = min(dp[-1][df + W], c)
    for d in range(-W, W + 1):
        if not dp[-2][d] == INF:
            dp[-1][df + d] = min(c + dp[-2][d], dp[-2][df + d], dp[-1][df + d])

print(("-1" if dp[N][W] == INF else dp[N][W]))
