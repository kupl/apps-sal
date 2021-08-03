from math import gcd


n = int(input())
a = [int(i) for i in input().split()]
cont = a.count(1)
if cont == 0:
    dp = [[0 for _ in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = a[i - 1]
    ans = 1e9
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            dp[i][j] = gcd(dp[i][j - 1], a[j - 1])
            if dp[i][j] == 1:
                ans = min(ans, j - i)
    if ans == 1e9:
        print(-1)
    else:
        print(n - 1 + ans)
else:
    print(n - cont)
