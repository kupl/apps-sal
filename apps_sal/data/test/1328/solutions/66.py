INF = float('inf')
(N, Ma, Mb, *ABC) = map(int, open(0).read().split())
M = 160010
dp = [0] + [INF] * M
for (a, b, c) in zip(*[iter(ABC)] * 3):
    T = dp[:]
    p = 401 * a + b
    for (i, dpi) in enumerate(dp):
        j = p + i
        if j > M:
            break
        if T[j] > dpi + c:
            T[j] = dpi + c
    dp = T
ans = INF
for i in range(1, M):
    (a, b) = divmod(i, 401)
    if Ma * b == Mb * a and ans > dp[i]:
        ans = dp[i]
print(-1 if ans == INF else ans)
