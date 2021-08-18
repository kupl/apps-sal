N, Ma, Mb = list(map(int, input().split()))
L = []
sum_a = 0
sum_b = 0
for _ in range(N):
    a, b, c = list(map(int, input().split()))
    sum_a += a
    sum_b += b
    L.append((a, b, c))

inf = 10 ** 9 + 7
dp = [[[inf] * (sum_b + 1) for _ in range(sum_a + 1)] for _ in range(N + 1)]

dp[0][0][0] = 0
for i in range(N):
    for a in range(sum_a + 1):
        for b in range(sum_b + 1):
            if 0 <= a - L[i][0] and 0 <= b - L[i][1]:
                dp[i + 1][a][b] = min(dp[i][a - L[i][0]]
                                      [b - L[i][1]] + L[i][2], dp[i][a][b])
            else:
                dp[i + 1][a][b] = dp[i][a][b]

min_cost = inf
for a in range(sum_a + 1):
    for b in range(sum_b + 1):
        if a * Mb == b * Ma and dp[N][a][b] != 0:
            min_cost = min(dp[N][a][b], min_cost)

print((min_cost if min_cost != inf else -1))
