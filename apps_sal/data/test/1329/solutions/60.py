n = int(input())
prime_factor = {1: 1} if n == 1 else {}
for i in range(2, n + 1):
    while i % 2 == 0:
        prime_factor[2] = prime_factor.get(2, 0) + 1
        i //= 2
    f = 3
    while f * f <= i:
        if i % f == 0:
            prime_factor[f] = prime_factor.get(f, 0) + 1
            i //= f
        else:
            f += 2
    if i != 1:
        prime_factor[i] = prime_factor.get(i, 0) + 1
m = len(prime_factor)
prime = list(prime_factor.keys())
dp = [[0] * 76 for _ in range(m + 2)]
dp[0][1] = 1
for i in range(m):
    for j in range(76):
        for k in range(prime_factor[prime[i]] + 1):
            if (v := (j * (k + 1))) < 76:
                dp[i + 1][v] += dp[i][j]
print(dp[m][75])
