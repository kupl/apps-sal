n = int(input())
MOD = 998244353
i2 = (MOD + 1) // 2

pi2 = [1]
for i in range(n):
    pi2.append((pi2[-1] * i2) % MOD)

ans = []
sum = n * i2 % MOD
for i in range((n + 1) // 2):
    if i >= 2:
        sum = (sum + pi2[n - 2 * i + 3] * (2 * i - 1)) % MOD
    ans.append(sum)

for i in range(n):
    print((ans[min(i, n - 1 - i)]))

