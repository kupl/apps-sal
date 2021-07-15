N = int(input())

patterns = []
patterns.append(1)

f = 6
a = 6
while a <= N:
    patterns.append(a)
    a *= f

f = 9
a = 9
while a <= N:
    patterns.append(a)
    a *= f

dp = [float('inf')] * (N + 1)
dp[0] = 0
for n in range(1, N + 1):
    for p in patterns:
        if n - p < 0:
            continue

        dp[n] = min(dp[n - p] + 1, dp[n])


print((dp[-1]))

