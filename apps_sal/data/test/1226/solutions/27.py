(n, a, b) = map(int, input().split())
MOD = 10 ** 9 + 7
fact = [1, 1]
factn = [1, n % MOD]
for i in range(2, b + 1):
    factn.append(factn[-1] * (n - i + 1) % MOD)
    fact.append(fact[-1] * i % MOD)
nca = factn[a] * pow(fact[a], MOD - 2, MOD) % MOD
ncb = factn[b] * pow(fact[b], MOD - 2, MOD) % MOD
ans = (pow(2, n, MOD) - 1 - nca - ncb) % MOD
if ans < 0:
    ans += MOD
print(ans)
