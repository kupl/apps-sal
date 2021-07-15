def dfs(current):
    for maps in Graph[current]:
        if maps in already:
            continue
        else:
            already.append(maps)
            dfs(maps)

n,m = map(int,input().split())
ans = 0
Edges = []
for _ in range(m):
    Edges.append([int(j)-1 for j in input().split()])

for i in range(m):
    egdes = Edges[0:i]+Edges[i+1:]
    Graph = [[] for _ in range(n)]
    for edge in egdes:
        Graph[edge[0]].append(edge[1])
        Graph[edge[1]].append(edge[0])
    already = []
    dfs(0)
    if len(already) != n:
        ans += 1
print(ans)
