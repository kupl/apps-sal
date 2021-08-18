MOD = 10**9 + 7
p = 1000009
fact = [0] * p
fact[0] = 1
for i in range(1, p):
    fact[i] = (fact[i - 1] * i) % MOD


def MI(a, MOD):
    return pow(a, MOD - 2, MOD)


def ncr(n, k, MOD):
    if n == k or k == 0:
        return 1
    if n < k:
        return 0
    return (fact[n] * MI(fact[k], MOD) % MOD * MI(fact[n - k], MOD) % MOD) % MOD


a, b, n = map(int, input().split())
good = [a, b]
j = -1
for i in range(10**5):
    j += 1
    good.append(good[j] * 10 + a)
    good.append(good[j] * 10 + b)
good.sort()
good = [i for i in good if n * min(a, b) <= i <= n * max(a, b)]
ans = 0
MOD = 10**9 + 7
for x in range(0, n + 1):
    if a * x + b * (n - x) in good:
        ans += ncr(n, x, MOD)
        ans %= MOD
print(ans)
