def dfs (a, vis, mr):
    mr[0]+=1
    vis[a]=1
    for g in range (0,len(r[a])):
        if (vis[r[a][g]]==1):
            continue
        dfs(r[a][g], vis, mr)
        
x=input("").split(' ')
nodes=int(x[0])
paths=int(x[1])
r=[]
for g in range (3000):
    r.append([])
vis=[0]*3000
for g in range (paths):
    m=input("").split(' ')
    rrr=int(m[0])
    rr=int(m[1])
    r[rrr].append(rr)
    r[rr].append(rrr)
ans=1
for g in range (1,nodes+1):
    mr=[0]
    if (vis[g]==1):
        continue
    l=dfs(g, vis,mr)
    ans*=pow(2,mr[0]-1)
print(ans)

