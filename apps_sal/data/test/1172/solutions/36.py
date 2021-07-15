def modinv(a,m):
    return pow(a,m-2,m)

import copy

S = input()
N = len(S)
dp = [[[0,0], [0,0,0], [0,0,0,0]] for i in range(N+1)]
mod = 10**9 + 7

for i in range(N):
    dp[i+1] = copy.deepcopy(dp[i])
    if S[i] == 'A':
        dp[i+1][0][0] += 1

    elif S[i] == 'B':
        for j in range(2):
            dp[i+1][1][j] = (dp[i+1][1][j] + dp[i][0][j])%mod

    elif S[i] == 'C':
        for j in range(3):
            dp[i+1][2][j] = (dp[i+1][2][j] + dp[i][1][j])%mod

    else:
        dp[i+1][0][1] += 1
        for j in range(2):
            dp[i+1][1][j+1] = (dp[i+1][1][j+1] + dp[i][0][j])%mod
        for j in range(3):
            dp[i+1][2][j+1] = (dp[i+1][2][j+1] + dp[i][1][j])%mod

Q = S.count('?')

inv3 = modinv(3,mod)
inv9 = inv3*inv3%mod
inv27 = inv9*inv3%mod
threeQ = pow(3,Q,mod)

ans = threeQ * (dp[N][2][0] + dp[N][2][1]*inv3 + dp[N][2][2]*inv9 + dp[N][2][3]*inv27) % mod
print(ans)
