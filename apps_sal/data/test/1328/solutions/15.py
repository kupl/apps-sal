N, Ma, Mb = list(map(int, input().split()))

dp = [[10**9 for i in range(401)] for j in range(401)]
dp[0][0] = 0

for _ in range(N):
    a, b, c = list(map(int, input().split()))
    for i in range(401)[::-1]:
        for j in range(401)[::-1]:
            if dp[i][j] != 10**9:
                dp[i + a][j + b] = min(dp[i + a][j + b], dp[i][j] + c)

ans = 10**9
for i in range(Ma, 401)[::Ma]:
    j = i // Ma * Mb
    if j >= 401:
        break
    ans = min(ans, dp[i][j])

if ans == 10**9:
    print((-1))
else:
    print(ans)
