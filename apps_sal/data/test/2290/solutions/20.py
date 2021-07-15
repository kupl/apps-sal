import sys
from sys import stdin,stdout
# sys.setrecursionlimit(300001)
visit=[]
def bfs(adj,i,m):
    queue = []
    queue.append(i)
    visit[i]=1
    while queue:
        h = queue.pop()
        if h>m:
            m=h
        visit[h]=1
        for j in adj[h]:
            if visit[j]==0:
                visit[j]=1
                queue.append(j)
    return m

# input = sys.stdin.readline()
n,m = stdin.readline().split()
n = int(n)
m = int(m)
adj = [[] for _ in range(n+1)]
while m>0:
    x,y = stdin.readline().split()
    x=int(x)
    y=int(y)
    adj[x].append(y)
    adj[y].append(x)
    m-=1
visit = [0]*(n+1)
result=0
count=0
k=0
for i in range(1,n+1):
    if visit[i]==0:
        if count>0 and i<k:
            result+=1
        if visit[i]==0 and len(adj[i])>0:
            count+=1
            k = bfs(adj,i,k)
stdout.write(str(result))
        
        

