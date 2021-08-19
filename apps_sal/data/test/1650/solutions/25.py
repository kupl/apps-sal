L = input()
MOD = 10 ** 9 + 7
l = len(L)
dp1 = [0] * (l + 1)
dp2 = [0] * (l + 1)
dp2[0] = 1
for i in range(l):
    dp1[i] %= MOD
    dp2[i] %= MOD
    if int(L[i]) == 1:
        dp1[i + 1] = 3 * dp1[i] + dp2[i]
        dp2[i + 1] = dp2[i] * 2
    else:
        dp1[i + 1] = 3 * dp1[i]
        dp2[i + 1] = dp2[i]
ans = dp1[l] + dp2[l]
print(ans % MOD)
