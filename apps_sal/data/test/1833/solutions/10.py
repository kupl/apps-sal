import math
n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = 1
mod = int(1000000000.0 + 7)
for el in a:
    sqrt = int(math.sqrt(el))
    for d in range(min(n, sqrt), 0, -1):
        if el % d == 0:
            if el / d > sqrt and el / d <= n:
                dp[el // d] = (dp[el // d] + dp[el // d - 1]) % mod
            dp[d] = (dp[d] + dp[d - 1]) % mod
res = 0
for i in range(1, n + 1):
    res = (res + dp[i]) % mod
print(res)
