(n, a) = (int(input()), list(map(int, input().split())))
(m, q) = (int(input()), list(map(int, input().split())))
dp = []
for i in range(n):
    dp += [i + 1] * a[i]
for x in q:
    print(dp[x - 1])
