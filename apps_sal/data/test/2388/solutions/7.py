import sys
input = sys.stdin.readline
N = int(input())
XD = [tuple(map(int, input().split())) for i in range(N)]
XD.sort()
MOD = 998244353
ns = [-1] * N

for i, (x, d) in reversed(list(enumerate(XD))):
    tmp = i
    while tmp < N - 1:
        nx, _ = XD[tmp + 1]
        if nx < x + d:
            tmp = ns[tmp + 1]
        else:
            break
    ns[i] = tmp

dp = [0] * (N + 1)
dp[N] = 1
for i in range(N - 1, -1, -1):
    dp[i] = (dp[i + 1] + dp[ns[i] + 1]) % MOD
print(dp[0])
