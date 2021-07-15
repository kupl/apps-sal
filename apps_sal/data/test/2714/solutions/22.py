import sys
from collections import defaultdict,deque
mod=998244353
def get(graph):
    vis=defaultdict(int)
    l=[]
    for i in range(1,n+1):
        if vis[i]==0:
            vis[i]=1
            q=deque()
            q.append(i)
            even=0
            odd=0
            while q:
                a=q.popleft()
                if vis[a]&1:
                    odd+=1
                else:
                    even+=1
                for x in graph[a]:
                    if vis[x]==0:
                        if vis[a]==1:
                            vis[x]=2
                        else:
                            vis[x]=1
                        q.append(x)
                    else:
                        if vis[x]==vis[a]:
                            return 0
            l.append([even,odd])
    m=len(l)
    x=pow(2,l[0][0],mod)
    y=pow(2,l[0][1],mod)
    ans=(x+y)%mod
    for i in range(1,m):
        x=pow(2,l[i][0],mod)
        y=pow(2,l[i][1],mod)
        z=(x+y)%mod
        ans=ans*z
        ans%=mod
    return ans%mod
    return False
'''def count(graph):
    vis=defaultdict(int)
    even=0
    odd=0
    for i in range(1,n+1):
        if vis[i]==0:
            vis[i]=1
            q=deque()
            q.append([i,0])
            while q:
                a,dis=q.popleft()
                if dis%2==0:
                    even+=1
                else:
                    odd+=1
                for x in graph[a]:
                    if vis[x]==0:
                        vis[x]=1
                        q.append([x,dis+1])
    return (even,odd)'''
t=int(sys.stdin.readline())
for _ in range(t):
    graph=defaultdict(list)
    
    n,m=list(map(int,sys.stdin.readline().split()))
    for i in range(m):
        u,v=list(map(int,sys.stdin.readline().split()))
        graph[u].append(v)
        graph[v].append(u)
    '''if _ == 5:
        print(graph)
    #print(graph,'graph')'''
    z=get(graph)
    #print(z,'z')
    print(z)

