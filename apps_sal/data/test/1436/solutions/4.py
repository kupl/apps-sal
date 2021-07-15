n=int(input())
a=list(map(int,input().split()))
ans=0
t=0
for i in range(n):
    if a[i]>0:
        t+=a[i]
    else:
        if t==0:
            ans+=1
        else:
            t-=1
print(ans)
