n = int(input())
a = list(map(int,input().split()))
a.sort()
ma = a[-1]

dp = [0]*(ma+1)

for i in range(1,n):
    if a[i]==a[i-1]:
        dp[a[i]]=1

for i in a:
    for j in range(i*2,ma+1,i):
        #if dp[j]==1:
            #break
        dp[j]=1
        
ans = 0
for i in a:
    if dp[i]==0:
        ans+=1
        
print(ans)
