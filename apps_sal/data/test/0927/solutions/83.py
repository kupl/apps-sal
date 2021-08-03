n, m = map(int, input().split())
A = list(map(int, input().split()))

d = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

INF = 10**18
dp = [-INF] * (n + 1)
dp[n] = 0
for i in reversed(range(1, n + 1)):
    for a in A:
        j = i - d[a]
        if j >= 0:
            dp[j] = max(dp[j], dp[i] * 10 + a)
print(dp[0])
