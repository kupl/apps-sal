
NMAX = 55
T = 2500
N, A = list(map(int, input().split()))
X = list([int(x) - A for x in input().split()])

dp = [[0]*5001 for i in range(NMAX)]  # i時点で総和がSになるものの個数

dp[0][T] = 1

for i in range(N):
    for s in range(5001):
        if s+X[i] > 5001 or dp[i][s] == 0:
            continue
        dp[i+1][s] += dp[i][s]
        dp[i+1][s+X[i]] += dp[i][s]

print((dp[N][T]-1))


