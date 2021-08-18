h, w, k = map(int, input().split())
mod = 10**9 + 7

if w == 1:
    print(1)
    return

dp = [[0] * w for i in range(h + 1)]
dp[0][0] = 1

l = [[0] * 3 for i in range(w)]

for i in range(2**(w - 1)):
    if "11" in bin(i):
        continue

    for j in range(w - 1):
        if (i >> j) & 1:
            l[j][2] += 1
            l[j + 1][0] += 1

fib = [1, 1]
for i in range(10):
    fib.append(fib[-1] + fib[-2])
for i in l:
    i[1] = fib[w] - sum(i)

for i in range(h):
    for j in range(w):
        dp[i + 1][j] += dp[i][j] * l[j][1] % mod
        if j != 0:
            dp[i + 1][j] += dp[i][j - 1] * l[j][0] % mod
        if j != w - 1:
            dp[i + 1][j] += dp[i][j + 1] * l[j][2] % mod
        dp[i + 1][j] %= mod

print(dp[-1][k - 1] % mod)
