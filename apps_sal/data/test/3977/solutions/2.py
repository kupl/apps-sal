n,m,k=map(int,input().split())
cap=[int(x)-1 for x in input().split()]
man=[[]for i in  range(n)]
visited=[False]*n
for i in range(m):
    a,b=map(int,input().split())
    man[a-1].append(b-1)
    man[b-1].append(a-1)
sv=[]
def dfs(v,p=None,r=None):
    p.append(v)
    r.append(len(man[v]))
    visited[v]=True
    for x in man[v]:
        if not visited[x]:
            dfs(x,p,r)
    return p,r
def analise():
    p,r=[],[]
    c=[]
    res=0
    mxcp=0
    mxcpr=0
    for i in range(n):
        if not visited[i]:
            p,r=[],[]
            p,r=dfs(i,p,r)
            a=len(p)
            b=sum(r)//2
            res+=((a-1)*a)//2-b
            if len(set(cap)&set(p))==1:
                if a>mxcp:
                    mxcp=a
                    mxcpr=b
            else:
                c.append([a,b])
    for x in c:
        res+=x[0]*mxcp
        mxcp+=x[0]
    return res
print(analise())
