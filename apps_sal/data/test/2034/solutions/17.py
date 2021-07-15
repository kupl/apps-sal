n,m=map(int,input().split())
g=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

a=0
v=[-1]*n
def dfs(x):
    nonlocal a
    s=[x]
    v[x]=-2
    while s:
        x=s.pop()
        for j in g[x]:
            if v[j]==-1:
                s.append(j)
                v[j]=x
            elif j!=v[x]:return 0
    return 1

for i in range(n):
    if v[i]==-1:
        a+=dfs(i)
print(a)
