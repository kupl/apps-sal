from collections import deque
import sys
n,m=list(map(int,sys.stdin.readline().split()))
a=[[] for i in range(n+1)]
d=deque([])
for i in range(m):
    b=list(map(int,sys.stdin.readline().split()))
    for j in b[2:]:
        a[b[1]].append(j)
        a[j].append(b[1])

ans=[1]*(n+1)
vis=[0]*(n+1)

for i in range(1,n+1):
    if vis[i]==0:
        vis[i]=1
        d.append(i)
    b=[]  
    while(d):
        # print(d,vis)
        p=d.popleft()
        b.append(p)
        for j in (a[p]):
            if vis[j]==0:
                d.append(j)
                vis[j]=1
    l=len(b)            
    # print(b)
    for j in b:
        ans[j]=l
print(*ans[1:])
    

        
        



