L = input()
mod = 10**9 + 7


N = [int(i) for i in L]
keta = len(N)
dp = [[0 for i in range(2)] for j in range(keta + 1)]
dp[0][0] = 1
#dp[0][0][1] =0
#dp[0][1][0] =0
#dp[0][1][1] =0

for i in range(keta):
    for smaller in [0, 1]:
        if 1:
            for x in range(2 if smaller else (N[i] + 1)):
                dp[i + 1][smaller | ((x == 0) & (N[i] == 1))] += dp[i][smaller] * (2 if x == 1 else 1)
                dp[i + 1][smaller | ((x == 0) & (N[i] == 1))] %= mod
print(((dp[keta][0] + dp[keta][1]) % mod))
