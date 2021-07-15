import sys
sys.setrecursionlimit(500*500)


n = int(input())
nodes = [list(map(int,input().split())) for _ in range(n-1)]
a = [[] for _ in range(n+1)]

for node in nodes:
    a[node[0]].append([node[1],node[2]])
    a[node[1]].append([node[0],node[2]])

depth = [-1] * (n+1)
depth[1] = 0

def dfs(a,s):
    for v in a[s]:
        if depth[v[0]] == -1:
            depth[v[0]] = depth[s] + v[1]
            dfs(a,v[0])    
dfs(a,1)
for d in depth[1:]:
    if d % 2 == 0:
        print((0))
    else:
        print((1))

