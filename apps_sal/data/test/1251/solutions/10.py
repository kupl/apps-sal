n = int(input())
t = [int(x) for x in input().split()]
t.insert(0, -1)

dp = [0] * (n + 3)
dp[1] = t[1]

for i in range(2, n + 1):
    dp[i] = t[i] + (i - 1)
    smallest = t[i]
    for j in range(i - 1, 0, -1):
        smallest = min(smallest, t[j])
        tmp = (dp[j] + (i - j - 1) + (t[i] - smallest))
        dp[i] = min(dp[i], tmp)

res = n
for i in range(1, n + 1):
    res = min(res, dp[i] + (n - i))
print(res)
