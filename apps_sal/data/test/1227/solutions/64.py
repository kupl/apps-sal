n = input()
k = int(input())
ln = len(n) + 1

dp = [[[0] * (ln) for _ in range(2)] for i in range(ln)]
dp[0][0][0] = 1
for i in range(len(n)):
    for smaller in range(2):
        x = int(n[i])
        t = 9 if smaller else x
        for j in range(t + 1):
            for knum in range(ln - 1):
                if j == 0:
                    dp[i + 1][int(smaller or j < x)][knum] += dp[i][smaller][knum]
                else:
                    dp[i + 1][int(smaller or j < x)][knum + 1] += dp[i][smaller][knum]
try:
    print(dp[-1][0][k] + dp[-1][1][k])
except:
    print(0)
