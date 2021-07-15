n = int(input())
li = [[] for i in range(0,n)]
for i in range(n-1):
    u, v, c = map(int,input().split())
    li[u].append((v,c))
    li[v].append((u,c))

mc = 0
cost = 0
visited = [False] * n
def DFS(num,visited,cost):
    nonlocal mc
    if cost > mc:
        mc = cost
    visited[num] = True
    for i in range(len(li[num])):
        if not visited[li[num][i][0]]:
            DFS(li[num][i][0],visited,cost+li[num][i][1])
DFS(0,visited,0)
print(mc)
