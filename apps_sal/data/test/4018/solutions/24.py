n, k = list(map(int, input().split()))
s = input()
last = [[-1 for i in range(26)] for j in range(n)]
for i in range(n):
    for j in range(26):
        if i != 0:
            last[i][j] = last[i-1][j]
    last[i][ord(s[i])-ord('a')] = i
dp = [[0 for i in range(n+1)] for j in range(n)]
for i in range(n):
    dp[i][1] = 1
for len in range(2, n+1):
    for i in range(1, n):
        for j in range(26):
            if last[i-1][j] != -1:
                dp[i][len] += dp[last[i-1][j]][len-1]
ans = 0
for len in range(n, 0, -1):
    cnt = 0
    for j in range(26):
        if last[n-1][j] != -1:
            cnt += dp[last[n-1][j]][len]
    if cnt >= k:
        ans += k*(n-len)
        k = 0
        break
    else:
        ans += cnt*(n-len)
        k -= cnt
if k == 1:
    ans += n
    k = 0
if k > 0:
    print(-1)
else:
    print(ans)

