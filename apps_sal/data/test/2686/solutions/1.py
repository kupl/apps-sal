n,m=map(int,input().strip().split())
connections={}
for _ in range(m):
    x,y=map(int,input().strip().split())
    if x not in connections.keys():
        connections[x]=[y]
    else:
        connections[x].append(y)
    if y not in connections.keys():
        connections[y]=[x]
    else:
        connections[y].append(x)
s,t=map(int,input().split())
distances=[-1]*(n+1)
distances[s]=0
unvisited=list(range(1,n+1))
while unvisited!=[]:
    min1=max(distances)
    v=-1
    flag=0
    for j in unvisited:
        if distances[j]!=-1 and min1>=distances[j]:
            min1=distances[j]
            v=j
    if v==-1:
        break
    unvisited.remove(v)
    for i in connections[v]:
        if i not in unvisited:
            continue
        if distances[i]==-1 or distances[i]>1+distances[v]:
            distances[i]=1+distances[v]
        if i==t:
            flag=1
            break
    if flag==1:
        break
if distances[t]==-1:
    distances[t]=0
print(distances[t])
