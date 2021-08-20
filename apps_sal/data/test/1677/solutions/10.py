n = int(input())
ls = list(map(int, input().split()))
dp = [[1 for i in range(n)] for j in range(n)]
laspos = [None] * (max(ls) + 1)
for i in range(n):
    for j in range(i):
        if laspos[ls[i]] is not None:
            dp[i][j] = 1 + dp[j][laspos[ls[i]]]
        else:
            dp[i][j] += 1
        laspos[ls[j]] = j
mx = -100000
for i in range(n):
    for j in range(n):
        mx = max(dp[i][j], mx)
print(mx)
