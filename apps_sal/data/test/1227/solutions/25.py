n = input()
k = int(input())
l = len(n)
dp = [[[0] * (k + 1) for j in range(2)] for i in range(l + 1)]
dp[0][0][0] = 1
for i in range(l):
    for j in range(2):
        for o in range(k + 1):
            for m in range(10):
                if not j and m > int(n[i]):
                    continue
                f = j or m < int(n[i])
                o2 = o + (m != 0)
                if o2 > k:
                    continue
                dp[i + 1][f][o2] += dp[i][j][o]
print(dp[-1][0][k] + dp[-1][1][k])
