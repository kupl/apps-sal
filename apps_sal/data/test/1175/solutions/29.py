m = 10**9 + 7
l, r = list(map(int, input().split()))
dp = [[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(61)]

dp[60][0][0][0] = 1

for i in reversed(list(range(60))):
    lb = l >> i & 1
    rb = r >> i & 1
    for j in range(2):
        for k in range(2):
            for s in range(2):
                pre = dp[i + 1][j][k][s]
                for x, y in [(0, 0), (0, 1), (1, 1)]:  # excpet for (1,0) (because of x<y)
                    nj, nk, ns = j, k, s
                    # s
                    if (s == 0 and x == 0 and y == 1):
                        continue  # skip for not x==y==1
                    if (s == 0 and x & y):
                        ns = 1
                    # j
                    if (j == 0 and lb == 1 and x == 0):
                        continue  # skip for x<l
                    if (j == 0 and lb == 0 and x == 1):
                        nj = 1
                    # k
                    if (k == 0 and rb == 0 and y == 1):
                        continue  # skip for r<y
                    if (k == 0 and rb == 1 and y == 0):
                        nk = 1

                    dp[i][nj][nk][ns] += pre
                    dp[i][nj][nk][ns] %= m

ans = 0
for j in range(2):
    for k in range(2):
        ans += dp[0][j][k][1]
        ans %= m
print(ans)
