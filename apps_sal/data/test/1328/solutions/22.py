import copy
(N, Ma, Mb) = list(map(int, input().split()))
ABC = [tuple(map(int, input().split())) for _ in range(N)]
(INF, W) = (10 ** 10, 10 * 10 * N)
dp = [[INF] * (2 * W + 1)]
for (a, b, c) in ABC:
    dp.append(copy.deepcopy(dp[-1]))
    df = a * Mb - b * Ma
    dp[-1][df] = min(c, dp[-1][df])
    for d in range(-W, W + 1):
        dp[-1][df + d] = min(c + dp[-2][d], dp[-1][df + d])
print('-1' if dp[N][0] == INF else dp[N][0])
