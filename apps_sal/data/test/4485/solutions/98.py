n,m = list(map(int,input().split()))
graph= dict()
for i in range(m):
    a,b  = list(map(int,input().split()))
    if(graph.get(a,-1)==-1):
        graph[a] = [b]
    else:
        graph[a].append(b)
    if (graph.get(b, -1) == -1):
        graph[b] = [a]
    else:
        graph[b].append(a)

q=[]
q.append((1,0))
visited = dict()
visited[1] = 1
ans = "IMPOSSIBLE"
while(len(q) != 0):
    front,d = q[0]
    q.pop(0)
    if(d>2):
        break
    if(front == n):
        ans = "POSSIBLE"
        break
    lst = graph.get(front,0)
    if(lst == 0):
        continue
    else:
        for i in lst:
            if(visited.get(i,-1)==-1):
                q.append((i,d+1))
print(ans)





