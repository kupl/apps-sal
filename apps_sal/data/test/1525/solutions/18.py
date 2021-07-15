h,w,K = map(int,input().split())
if w == 1:
    print(1)
    return
K -= 1
mod = 1000000007
dp = [[0]*(w) for _ in range(h+1)]
for i in range(w): dp[0][0] = 1

for i in range(h):
    for j in range(1<<(w-1)):
        invalid = False
        for k in range(w-1):
            if j>>k & 1 and j>>(k+1) & 1:
                invalid = True
                break
        if invalid: continue
        used = [False]*w
        for k in range(w):
            if used[k]: continue
            if j>>k & 1:
                dp[i+1][k] = (dp[i+1][k]+dp[i][k+1])%mod
                dp[i+1][k+1] = (dp[i+1][k+1]+dp[i][k])%mod
                used[k] = True
                used[k+1] = True
            else:
                dp[i+1][k] = (dp[i+1][k]+dp[i][k])%mod
                used[k] = True
# for i in range(h+1): print(dp[i])
print(dp[h][K])
