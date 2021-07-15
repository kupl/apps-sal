n,d=map(int,input().split())
s=str(input())
p=0
ans=0
while p<n:
    f=0
    if p==n-1:
        break
    for i in range(p+1,min(p+d+1,n)):
        if s[i]=='1':
            f=1
            pp=i
    if f==0:
        print(-1)
        #print(p,pp)
        return
    else:
        p=pp
        ans+=1
print(ans)
