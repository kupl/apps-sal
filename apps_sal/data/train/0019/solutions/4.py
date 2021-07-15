n=int(input())
for i in range(n):
    n,k,d=list(map(int,input().split()))
    a=[int(j) for j in input().split()]
    dv=dict()
    s=set()
    mn=n
    for j in range(n):
        if j>=d:
            mn=min(mn,len(s))
            t=a[j-d]
            dv[t]-=1
            if dv[t]==0:
                s.discard(t)
        t=a[j]
        if t in dv:
            dv[t]+=1
        else:
            dv[t]=1
        s.add(t)
    mn=min(mn,len(s))
    print(mn)

