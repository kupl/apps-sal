n,m,k=map(int,input().split())
c=list(map(int,input().split()))
g=[[]for _ in range(n)]
for _ in range(m):
    l,r=map(int,input().split())
    g[l-1].append(r-1)
    g[r-1].append(l-1)
v=[-1]*n
o=0
for i in range(n):
    if v[i]==-1:
        s=[i]
        v[i]=1
        q={}
        while s:
            x=s.pop()
            if c[x] not in q:q[c[x]]=0
            q[c[x]]+=1
            for j in g[x]:
                if v[j]==-1:
                    v[j]=1
                    s.append(j)
        r,k=0,0
        for b in q:
            k=max(k,q[b])
            r+=q[b]
        o+=r-k
print(o)
