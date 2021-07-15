n=int(input())
from collections import defaultdict,deque
g=defaultdict(list)
from sys import stdin
for i in range(n-1):
    h,m=list(map(int, stdin.readline().split()))
    g[h-1].append(m-1)
    g[m-1].append(h-1)
vis=[0]*n
c=[0]*n
c[0]=1
q=deque()
q.append(0)
while q:
    node=q.popleft()
    vis[node]=1
    s=set()
    for i in g[node]:
        if vis[i]==1:
            s.add(c[i])
    p=[]
    s.add(c[node])
    l=len(s)
    j=0
    k=1
    while l+j<=len(g[node])+2:
        r=0
        while r==0:
            if k not in s:
                p.append(k)
                r=1
            k+=1
        j+=1
    j=0
    for i in g[node]:
        if vis[i]==0:
            c[i]=p[j]
            j+=1
            q.append(i)

print(max(c))
print(*c)
        
            

