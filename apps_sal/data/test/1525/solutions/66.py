def isok(n):
    for i in range(w-2):
        if n >> i & 1 and n >> (i+1) & 1:
            return False
    return True
mod = 10**9+7
h,w,k = map(int,input().split())
h += 1
if w == 1:
    print(1)
    return
if w == 2:
    print(2**(h-2))
    return
dp = [[0]*(w+1) for _ in range(h+1)]
dp[1][1] = 1
amida = [0]*(w)
noamida = [0]*(w+1)
for i in range(2**(w-1)):
    if isok(i):
        for j in range(w-1):
            amida[j+1] += i >> j & 1
        for j in range(w-2):
            if i >> j & 1 == 0 and i >> (j+1) & 1 == 0:
                noamida[j+2] += 1
        if i >> 0 & 1 == 0:
                noamida[1] += 1
        if i >> (w-2) & 1 == 0:
                noamida[w] += 1
for i in range(1,h):
    dp[i+1][1] = (dp[i][2]*amida[1]+dp[i][1]*noamida[1]) % mod
    dp[i+1][w] = (dp[i][w-1]*amida[w-1]+dp[i][w]*noamida[w]) % mod
    for j in range(2,w):
        dp[i+1][j] = (dp[i][j-1]*amida[j-1]+dp[i][j+1]*amida[j]+dp[i][j]*noamida[j]) % mod
print(dp[h][k])
