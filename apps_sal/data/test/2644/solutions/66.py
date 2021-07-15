n=int(input())
p=list(map(int,input().split()))
now=1
ans=[]
for i in range(n):
    if p[i]==now:
        for j in range(i-1,now-2,-1):
            p[j],p[j+1]=p[j+1],p[j]
            ans.append(j+1)
        now=i+1
if p!=[i for i in range(1,n+1)] or len(ans)!=n-1:
    print(-1)
else:
    for i in ans:
        print(i)
