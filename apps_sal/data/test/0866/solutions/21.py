fact = [None] * 1000001
inv = [0, 1]
finv = [1, 1]

x, y = map(int, input().split())
total = x + y
ans = 0
MOD = 10**9 + 7

if total % 3 == 0 and max(x, y) <= min(x, y) * 2:
    fact[1] = 1
    for i in range(2, 1000001):
        fact[i] = fact[i - 1] * i % MOD
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
        finv.append(finv[-1] * inv[-1] % MOD)
    step = int(total / 3)
    sa = abs(x - y)
    a = int((step - sa) / 2)
    b = int((step + sa) / 2)
    ans = fact[step] * finv[a] * finv[b] % MOD
print(ans)
