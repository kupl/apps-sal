n=int(input())
c1=list(map(int,input().split()))
c2=list(map(int,input().split()))
c3=list(map(int,input().split()))
ans=-1
edges={}
degree=[0]*n
for i in range(n-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    degree[u]+=1
    degree[v]+=1
    if u not in edges:
        edges[u]=[v]
    else :
        edges[u].append(v)
    if v not in edges:
        edges[v]=[u]
    else :
        edges[v].append(u)
import sys
if max(degree)>2:
    print(-1)
    return
bfs=[]
for i in range(n):
    if degree[i]==1:
        bfs.append(i)
        break
visited=[0]*n
visited[bfs[0]]=1
cost123=c1[bfs[0]]
cost132=c1[bfs[0]]
cost213=c2[bfs[0]]
cost231=c2[bfs[0]]
cost312=c3[bfs[0]]
cost321=c3[bfs[0]]
turn=1
colors=[0]*n
colors[bfs[0]]=1
while bfs:
    temp=[]
    for u in bfs:
        for v in edges[u]:
            if visited[v]==0:
                colors[v]=turn+1
                visited[v]=1
                temp.append(v)
                if turn==0:
                    cost123+=c1[v]
                    cost132+=c1[v]
                    cost213+=c2[v]
                    cost231+=c2[v]
                    cost312+=c3[v]
                    cost321+=c3[v]
                if turn==1:
                    cost123+=c2[v]
                    cost132+=c3[v]
                    cost213+=c1[v]
                    cost231+=c3[v]
                    cost312+=c1[v]
                    cost321+=c2[v]
                if turn==2:
                    cost123+=c3[v]
                    cost132+=c2[v]
                    cost213+=c3[v]
                    cost231+=c1[v]
                    cost312+=c2[v]
                    cost321+=c1[v]
                
    bfs=temp
    turn+=1
    turn=turn%3
x=min(cost123,cost132,cost213,cost231,cost312,cost321)
print(x)
if x==cost132:
    for i in range(n):
        if colors[i]==3:
            colors[i]=2
        elif colors[i]==2:
            colors[i]=3
elif x==cost213:
    for i in range(n):
        if colors[i]==1:
            colors[i]=2
        elif colors[i]==2:
            colors[i]=1
elif x==cost231:
    for i in range(n):
        if colors[i]==1:
            colors[i]=2
        elif colors[i]==2:
            colors[i]=3
        else :
            colors[i]=1
elif x==cost312:
    for i in range(n):
        if colors[i]==1:
            colors[i]=3
        elif colors[i]==2:
            colors[i]=1
        else :
            colors[i]=2
elif x==cost321:
    for i in range(n):
        if colors[i]==1:
            colors[i]=3
        elif colors[i]==3:
            colors[i]=1
print(*colors,sep=" ")
    
