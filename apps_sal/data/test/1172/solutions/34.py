S = input()
N = len(S)
mod = 10 ** 9 + 7
dp1 = [0 for _ in range(N + 1)]
dp2 = [0 for _ in range(N + 1)]
dp3 = [0 for _ in range(N + 1)]
dp4 = [0 for _ in range(N + 1)]
dp1[0] = 1

for i in range(N):
    if S[i] == '?':
        dp1[i + 1] += 3 * dp1[i]
        dp2[i + 1] += 3 * dp2[i] + dp1[i]
        dp3[i + 1] += 3 * dp3[i] + dp2[i]
        dp4[i + 1] += 3 * dp4[i] + dp3[i]
    else:
        dp1[i + 1] += dp1[i]
        dp2[i + 1] += dp2[i]
        dp3[i + 1] += dp3[i]
        dp4[i + 1] += dp4[i]
    if S[i] == 'A':
        dp2[i + 1] += dp1[i]
    if S[i] == 'B':
        dp3[i + 1] += dp2[i]
    if S[i] == 'C':
        dp4[i + 1] += dp3[i]
    dp1[i + 1] %= mod
    dp2[i + 1] %= mod
    dp3[i + 1] %= mod
    dp4[i + 1] %= mod

print(dp4[N])
