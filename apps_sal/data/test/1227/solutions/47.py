strN = input().rstrip()
K = int(input())
maxD = len(strN)
dp = [[[0] * (K + 1) for j in range(2)] for i in range(maxD + 1)]
dp[0][0][0] = 1
for (d, Nd) in enumerate(strN):
    Nd = int(Nd)
    for isLtN in range(2):
        for numNot0 in range(K + 1):
            for x in range(10):
                if not isLtN and x > Nd:
                    continue
                isLtN2 = isLtN or x < Nd
                numNot02 = numNot0 + (x != 0)
                if numNot02 > K:
                    continue
                dp[d + 1][isLtN2][numNot02] += dp[d][isLtN][numNot0]
ans = dp[-1][0][K] + dp[-1][1][K]
print(ans)
