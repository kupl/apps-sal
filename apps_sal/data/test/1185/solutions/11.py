n, m, k = list(map(int, input().split()))
l = list(map(int, input().split()))
if(m == 1):
    l.sort()
    ans = 0
    for i in range(k):
        ans += l[n - 1 - i]
    print(ans)
    return
pres = []
s = 0
pres.append(0)
for i in l:
    s += i
    pres.append(s)
dp = [[0 for i in range(n + 1)]for j in range(k + 1)]

for i in range(k + 1):
    for j in range(n + 1):
        if(i == 0):
            dp[i][j] = 0
        elif(j < i * m):
            dp[i][j] = 0
        elif(j == i * m):
            dp[i][j] = pres[j]
        else:
            dp[i][j] = max(dp[i][j - 1], pres[j] - pres[j - m] + dp[i - 1][j - m])
print(dp[k][n])
