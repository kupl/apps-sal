MOD = 10**9 + 7
S = input()
res = 0
dp0 = 1  # ''
dp1 = 0  # 'a'
dp2 = 0  # 'ab'
dp3 = 0  # 'abc'

for c in S:
    if c == 'A':
        dp1 = (dp0 + dp1) % MOD
    elif c == 'B':
        dp2 = (dp1 + dp2) % MOD
    elif c == 'C':
        dp3 = (dp2 + dp3) % MOD
    else:
        dp3 = (dp3 * 3 + dp2) % MOD
        dp2 = (dp2 * 3 + dp1) % MOD
        dp1 = (dp1 * 3 + dp0) % MOD
        dp0 = (dp0 * 3) % MOD
print(dp3)
