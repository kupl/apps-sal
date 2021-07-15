n,m=map(int,input().split())
E=[[] for i in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    E[x]+=[y]
    E[y]+=[x]
f=[0]*(n+1)
def bfs(nom):
    l=[(nom,0)]
    f[nom]=1
    k=1
    while len(l):
        nom,pre=l.pop()
        for x in E[nom]:
            if x!=pre:
                if f[x]: k=0
                else:
                    f[x]=1
                    l+=[(x,nom)]
    return k
ans=0
for i in range(1,n+1):
    if f[i]==0: ans+=bfs(i)
print(ans)
