from collections import deque
n=int(input())
e=[[] for _ in range(n+1)]
dist=[-1]*(n+1)
for i in range(n-1):
    a,b,c=map(int,input().split())
    e[a].append((b,c))
    e[b].append((a,c))
q,k=map(int,input().split())
a=deque()
a.append((k,0))
while a:
    x,d=a.popleft()
    dist[x]=d
    for j,nc in e[x]:
        if dist[j]!=-1:
            continue
        else:
            a.append((j,d+nc))
ans=[]
for i in range(q):
    x,y=map(int,input().split())
    ans.append(dist[x]+dist[y])
print(*ans,sep="\n")
