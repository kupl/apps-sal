k1, k2, k3 = map(int, input().split())
s = [set(map(int, input().split())) for _ in range(3)]

inf = 10**9
dp = [[inf]*3 for _ in range(k1+k2+k3+1)]
dp[0][0] = 0


for i in range(1, k1+k2+k3+1):
    for j in range(3):
        for k in range(j, 3):
            dp[i][k] = min(dp[i][k], dp[i-1][j] + (i not in s[k]))

print(min(dp[-1]))
