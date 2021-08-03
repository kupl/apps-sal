n, m, k = map(int, input().split())
mod = 10**9 + 7
rng = n * m + 10
fctr = [1]
finv = [1]
for i in range(1, rng):
    fctr.append(fctr[-1] * i % mod)
for i in range(1, rng):
    finv.append(pow(fctr[i], mod - 2, mod))


def cmb(n, k):
    if n < 0 or k < 0:
        return 0
    else:
        return fctr[n] * finv[n - k] * finv[k] % mod


cost = [[0 for i in range(m + 1)] for j in range(n + 1)]
cost[1][1] = ((n - 1) + (m - 1)) * n * m // 2
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j > 1:
            cost[i][j] = cost[i][j - 1] - (m - 2 * (j - 1)) * n
        elif i > 1:
            cost[i][j] = cost[i - 1][j] - (n - 2 * (i - 1)) * m
ans = 0
for i in cost:
    ans = (ans + sum(i)) % mod
ans = ans * pow(2, mod - 2, mod) % mod
ans = ans * cmb(n * m - 2, k - 2) % mod
print(ans)
