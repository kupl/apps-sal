n,m = list(map(int,input().split()))
s = input()
dp = [0]*(n+1)
r = n

for i in range(n-1,-1,-1):
    if int(s[i]) == 1:
        dp[i] = -1
        continue
    while r > i+m:r-=1
    while dp[r] == -1:r -= 1
    if r == i:
        print((-1))
        return
    dp[i] = dp[r]+1
now = 0
ans = []
for i in range(n+1):
    if dp[i] == -1:continue
    if dp[i] != dp[now]:
        ans.append(i-now)
        now = i
print((*ans))
        
    

