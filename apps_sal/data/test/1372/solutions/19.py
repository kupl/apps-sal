(h, n) = map(int, input().split())
lis = []
amax = 0
for i in range(n):
    (a, b) = map(int, input().split())
    if a > amax:
        amax = a
    lis.append([a, b])
dp = [0] * (h + amax)
for i in range(1, h + amax):
    dp[i] = min((dp[i - a] + b for (a, b) in lis))
print(dp[h])
