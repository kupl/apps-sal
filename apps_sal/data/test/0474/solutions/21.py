n=int(input())
a=list(map(int,input().split()))
mx=max(a)
cnt=0
ans=0
for i in range(n):
    if a[i]==mx:
        cnt+=1
    else:
        ans=max(ans,cnt)
        cnt=0
ans=max(ans,cnt)
print(ans)

