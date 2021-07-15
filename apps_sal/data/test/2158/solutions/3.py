def dfs(u,cur):
    nonlocal ans
    vis[u]=True
    flag=True
    for x in vec[u] :
        v=x[0]
        c=x[1]
        if not vis[v] :
            dfs(v,cur+c)
            flag=False
    if flag:
        ans=max(cur,ans)
ans=0
vec=[]
vis=[]
i=0
n=int(input())
while(i<n) :
    vec.append([])
    vis.append(False)
    i+=1
i=1
while(i<n):
    u,v,c=(int(x) for x in input().split(' '))
    vec[u].append((v,c))
    vec[v].append((u,c))
    i+=1
dfs(0,0)
print(ans)

