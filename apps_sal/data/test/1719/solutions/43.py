n = int(input())
mod = pow(10, 9) + 7
alph = list('AGCT')
ng1 = [list('AGC'), list('ACG'), list('GAC')]
dp = [0] * 64
for i in range(4):
    for j in range(4):
        for k in range(4):
            if not [alph[i], alph[j], alph[k]] in ng1:
                dp[16 * i + 4 * j + k] = 1
for _ in range(n - 3):
    dp0 = [0] * 64
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if not [alph[j], alph[k], alph[l]] in ng1:
                        if not ([alph[i], alph[l]] == list('AC') and (alph[j] == 'G' or alph[k] == 'G')):
                            dp0[16 * j + 4 * k + l] += dp[16 * i + 4 * j + k]
                            dp0[16 * j + 4 * k + l] %= mod
    for i in range(64):
        dp[i] = dp0[i]
ans = sum(dp) % mod
print(ans)
