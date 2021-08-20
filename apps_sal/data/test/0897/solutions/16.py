(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
MOD = int(1000000000.0 + 7)
m2 = pow(2, MOD - 2, MOD)
mm = pow(m, MOD - 2, MOD)
f = 1
ans = 0
for (i, j) in zip(a, b):
    if i == 0 and j == 0:
        ans += (m - 1) * m2 * mm * f
        ans %= MOD
        f = f * mm % MOD
    elif i == 0:
        ans += (m - j) * f * mm
        ans %= MOD
        f = f * mm % MOD
    elif j == 0:
        ans += (i - 1) * f * mm
        ans %= MOD
        f = f * mm % MOD
    elif i > j:
        ans += f
        ans %= MOD
        break
    elif i < j:
        break
print(ans)
