(n, m) = map(int, input().split())
al = [0] * (n + 2)
for _ in range(m):
    al[int(input())] += 1
dp = [0] * (n + 2)
dp[0] = 1
for i in range(n):
    if al[i] != 0:
        continue
    else:
        dp[i + 1] += dp[i]
        dp[i + 2] += dp[i]
print(dp[n] % (10 ** 9 + 7))
