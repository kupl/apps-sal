n = int(input())
a = list(map(int, input().split()))

p = list(range(n))
p.sort(key=lambda i: a[i])

dp = [0] * (n + 1)

for i in range(n):
    for j in range(n - i):
        dp[j] = max(dp[j] + a[p[i]] * abs(p[i] - (j + i)), dp[j + 1] + a[p[i]] * abs(p[i] - j))

print((dp[0]))
