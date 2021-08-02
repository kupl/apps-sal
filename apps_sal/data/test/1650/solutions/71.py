MOD = 10**9 + 7

L = input()

dp1 = [0] * (len(L) + 1)
dp0 = [1] * (len(L) + 1)

for i in range(len(L)):
    dp1[i + 1] = dp1[i] * 3 + dp0[i] * (L[i] == "1")
    dp0[i + 1] = dp0[i] * (2 if L[i] == "1" else 1)
    dp1[i + 1] %= MOD
    dp0[i + 1] %= MOD

ans = dp1[-1] + dp0[-1]
print(ans % MOD)
