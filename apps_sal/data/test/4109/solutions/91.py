n,m,x=[int(i) for i in input().split()]
c=[]
arr=[[] for i in range(n)]
for i in range(n):
    l=[int(i) for i in input().split()]
    c.append(l[0])
    arr[i]=l[1:]

inf=10**18
ans=inf

limit=2**n
for bit in range(1,limit):
    sum=[0 for i in range(m)]
    cost=0
    for i in range(n):
        if (1<<i & bit):
            cost+=c[i]
            for j in range(m):
                sum[j]+=arr[i][j]
    flag=1
    for i in range(m):
        if sum[i]<x:
            flag=0
            break
    if flag==0:
        continue
    ans=min(ans,cost)
if ans!=inf:
    print(ans)
else:
    print((-1))

