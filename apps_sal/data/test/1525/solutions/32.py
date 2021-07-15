MOD = 10 ** 9 + 7
h, w, k = list(map(int, input().split()))
dp = [0] * w
dp[0] = 1

fdp = [[0, 0] for _ in range(w)]
fdp[0][0] = 1
for i in range(w - 1):
    fdp[i+1][0] += fdp[i][0]
    fdp[i+1][1] += fdp[i][0]
    fdp[i+1][0] += fdp[i][1]

def f(i):
    if i < 0:
        return 1
    return fdp[i][0] + fdp[i][1]

for _ in range(h):
    ndp = [0] * w
    for i in range(w):
        ndp[i] = (ndp[i] + dp[i] * f(i - 1) * f(w - i - 2))  % MOD
        if i + 1 < w:
            ndp[i+1] = (ndp[i+1] + dp[i] * f(i - 1) * f(w - i - 3)) % MOD
        if i - 1 >= 0:
            ndp[i-1] = (ndp[i-1] + dp[i] * f(i - 2) * f(w - i - 2)) % MOD
    dp = ndp
print((dp[k-1]))

