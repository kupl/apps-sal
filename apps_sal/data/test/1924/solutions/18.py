MOD = 10 ** 9 + 7
table_len = 2 * 10 ** 6 + 10
fac = [1, 1]
for i in range(2, table_len):
    fac.append(fac[-1] * i % MOD)
finv = [0] * table_len
finv[-1] = pow(fac[-1], MOD - 2, MOD)
for i in range(table_len - 1, 0, -1):
    finv[i - 1] = finv[i] * i % MOD


def comb(a, b):
    return fac[a + b] * finv[a] * finv[b] % MOD


(r1, c1, r2, c2) = map(int, input().split())
ans = (comb(r1, c1) + comb(r2 + 1, c2 + 1) - comb(r1, c2 + 1) - comb(r2 + 1, c1)) % MOD
print(ans)
