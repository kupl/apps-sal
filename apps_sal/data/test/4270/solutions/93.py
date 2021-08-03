n = int(input())
v = list(map(float, input().split()))

v.sort()
dp = [0] * (n - 1)

for i in range(n - 1):
    dp[i] += (v[i] + v[i + 1]) / 2
    v[i + 1] = dp[i]
print((dp[-1]))
