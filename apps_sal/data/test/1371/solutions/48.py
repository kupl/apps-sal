s = int(input())
cnt = 0
MOD = 10 ** 9 + 7

fact = [0] * 3000
fact_inv = [0] * 3000
fact[0] = 1

for i in range(1, 3000):
    fact[i] = fact[i - 1] * i % MOD
fact_inv[3000 - 1] = pow(fact[3000 - 1], MOD - 2, MOD)

for i in range(3000 - 1, 0, -1):
    fact_inv[i - 1] = fact_inv[i] * i % MOD


def nCk(n, k):
    return fact[n] * fact_inv[k] * fact_inv[n - k] % MOD


for n in range(1, s):
    if n * 3 > s:
        break
    cnt += nCk(s - 3 * n + n - 1, n - 1)
    cnt %= MOD

print(cnt)
