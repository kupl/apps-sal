
H,N = list(map(int, input().split()))
magics = [tuple(map(int, input().split())) for _ in range(N)]

max_a = max(magics, key=lambda x: x[0])[0]

dp = [0] * (H + max_a + 1)

for i in range(2,H + max_a + 1):
    temp = 10**10
    for a,m in magics:
        if temp > dp[i-a] + m:
            temp = dp[i-a] + m

    dp[i] = temp

print((min(dp[H+1:])))

