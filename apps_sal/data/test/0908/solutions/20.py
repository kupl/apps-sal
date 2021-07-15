n = int(input())
c = list(map(int, input().split()))
s = []
for _ in range(n):
    s.append(input())
dp = [[float('inf')] * 2 for _ in range(n)]
dp[0][0] = 0
dp[0][1] = c[0]
for i in range(1, n):
    for j in range(2):
        cost = float('inf')
        base_cost = 0
        s_ = s[i]
        if j == 1:
            base_cost = c[i]
            s_ = s_[::-1]
        for k in range(2):
            target_cost = dp[i - 1][k]
            target_s = s[i - 1]
            if k == 1:
                target_s = target_s[::-1]
            if target_s <= s_:
                cost = min(cost, base_cost + target_cost)
            else:
                cost = min(cost, float('inf'))
        dp[i][j] = cost
ans = min(dp[n - 1][0], dp[n - 1][1])
if ans == float('inf'):
    print(-1)
else:
    print(ans)

