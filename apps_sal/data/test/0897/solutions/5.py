MOD = 10 ** 9 + 7
(n, m) = [int(x) for x in input().split()]
s1 = [int(x) for x in input().split()]
s2 = [int(x) for x in input().split()]
mi = pow(m, MOD - 2, MOD)
m2 = pow(2, MOD - 2, MOD)
ans = 0
mul = 1
for (a, b) in zip(s1, s2):
    if a == 0 and b == 0:
        ans = (ans + mul * ((m - 1) * (mi * m2))) % MOD
        mul = mul * mi % MOD
    elif a == 0:
        ans = (ans + mul * (m - b) * mi) % MOD
        mul = mul * mi % MOD
    elif b == 0:
        ans = (ans + mul * (a - 1) * mi) % MOD
        mul = mul * mi % MOD
    elif a > b:
        ans = (ans + mul * 1) % MOD
        break
    elif a == b:
        pass
    elif a < b:
        break
print(ans % MOD)
