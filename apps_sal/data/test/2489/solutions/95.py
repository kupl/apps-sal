n=int(input())
a=list(map(int,input().split()))
ans=0
a.sort()
num=a[-1]
dp=[True]*num
seen=[0]*num
for i in range(n):
    num2=a[i]
    if dp[num2-1]==True:
        if seen[num2-1]==1:
            dp[num2-1]=False
        for j in range(2,num//num2+1):
            dp[j*num2-1]=False
    seen[a[i]-1]=1
ans=0
for i in range(n):
    if dp[a[i]-1]==True:
        ans+=1
print(ans)

