N,M=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(M)]
r=0
for m in range(M):
    c=[[] for i in range(N)]
    for i,(a,b) in enumerate(AB):
        if i!=m:
            c[a-1].append(b-1)
            c[b-1].append(a-1)
    q=[0]
    v=[1]+[0]*(N-1)
    while q:
        p=q.pop()
        for n in c[p]:
            if v[n]==0:
                v[n]=1
                q.append(n)
    if 0 in v:
        r+=1
print(r)
