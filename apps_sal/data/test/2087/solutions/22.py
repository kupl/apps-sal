MOD = 998244353

a, b, c = map(int, input().split())
sa = a * (a + 1) // 2 % MOD
sb = b * (b + 1) // 2 % MOD
sc = c * (c + 1) // 2 % MOD
ans = sa * sb % MOD * sc % MOD
if ans < 0:
    ans += MOD
print(ans)
