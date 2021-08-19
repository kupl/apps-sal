(n, k) = tuple(map(int, input().rstrip().split()))
s = input().rstrip()
cur = int(2 * pow(10, 5) * (2 * pow(10, 5) + 1) / 2) + 1
cost = [0] * (n + 1)
dp = [0]
for i in range(n, 0, -1):
    if s[i - 1] == '1':
        cur = i
    cost[i] = cur
for i in range(1, n + 1):
    dp.append(dp[-1] + i)
    cs = cost[max(i - k, 1)]
    if cs <= i + k:
        dp[i] = min(dp[i], dp[max(1, cs - k) - 1] + cs)
print(dp[n])
