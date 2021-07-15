n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
matchlist = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
numberlist = []
for i in range(m):
    numberlist.append(matchlist[a[i]])
numberlist = set(numberlist)
#dp[i]:i本でのmax桁
dp = [-10000000]*(n+1)
dp[0] = 0
for i in range(n):
    for j in numberlist:
        if i+j <= n:
            dp[i+j] = max(dp[i+j], dp[i]+1)


ans = []
d = dp[n]
a.sort(reverse = True)
for i in range(d):
    for j in a:
        if n - matchlist[j] >= 0:
            if dp[n] == dp[n-matchlist[j]] + 1:
                n -= matchlist[j]
                ans.append(j)
                break
print(("".join(map(str,ans))))

