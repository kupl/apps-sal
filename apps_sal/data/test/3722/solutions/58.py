import sys
readline = sys.stdin.readline
N = int(readline())
caa = readline().strip() == 'A'
cab = readline().strip() == 'A'
cba = readline().strip() == 'A'
cbb = readline().strip() == 'A'
MOD = 10 ** 9 + 7
if not cab:
    (caa, cbb) = (cbb ^ 1, caa ^ 1)
    cab ^= 1
    cba ^= 1
if N == 2:
    print(1)
elif N == 3:
    print(1)
elif caa:
    print(1)
else:
    if cba:
        dp = [0] * (N - 2)
        dp1 = [0] * (N - 2)
        dp[0] = 1
        dp1[0] = 0
        for i in range(1, N - 2):
            dp[i] = (dp[i - 1] + dp1[i - 1]) % MOD
            dp1[i] = dp[i - 1]
        ans = (dp[N - 3] + dp1[N - 3]) % MOD
    else:
        ans = pow(2, N - 3, MOD)
    print(ans)
