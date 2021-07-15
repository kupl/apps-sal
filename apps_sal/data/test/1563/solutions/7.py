n,m = list(map(int,input().strip().split()))
color = list(map(int,input().strip().split()))
g = [[] for  i in range(n)]
colors = {i:set() for i in sorted(color)}
for i in range(m):
    u,v =list(map(int,input().strip().split()))
    u -= 1
    v -= 1
    if color[u] != color[v]:
        colors[color[u]].add(color[v])
        colors[color[v]].add(color[u])
print(max(colors,key = lambda x : len(colors[x])))
