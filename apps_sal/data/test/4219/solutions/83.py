n=int(input())
xy=[[[]] for _ in range(n)]
for i in range(n):
    a=int(input())
    xy[i]=[list(map(int,input().split())) for _ in range(a)]
ans=0
for i in range(2**n):
    tmp=[0]*n
    flag1=True
    for j in range(n):
        if (i>>j)&1:
            tmp[j]=1
    for k in range(n):
        flag2=True
        if tmp[k]==1:
            for x,y in xy[k]:
                if tmp[x-1]!=y:
                    flag1=False
                    flag2=False
                    break
        if not flag2:
            break
    if flag1:
        ans=max(ans,sum(tmp))
print(ans)
