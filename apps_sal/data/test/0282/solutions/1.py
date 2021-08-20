(n, d) = [int(i) for i in input().split()]
a = input()
dp = [1000000000.0] * n
dp[0] = 0
for i in range(1, n):
    if a[i] == '0':
        continue
    for j in range(1, d + 1):
        if i - j < 0:
            break
        dp[i] = min(dp[i], dp[i - j] + 1)
print(dp[-1] if dp[-1] != 1000000000.0 else -1)
