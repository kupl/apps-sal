MOD = 10**9 + 7


def combi(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % MOD


N = 2000
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

S = int(input())

cnt = 0
for i in range(1, S):
    if 3 * i > S:
        break
    x = S - 3 * i
    c = combi(x + i - 1, i - 1)
    # print(x, i, c)
    cnt = (cnt + c) % MOD

print(cnt)
