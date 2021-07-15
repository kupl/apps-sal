n = int(input())
MAX = 10**5
adj = [[[] for u in range(MAX+1)] for t in range(2)]
vis = [[False for u in range(MAX+1)] for t in range(2)]
for i in range(n):
	x, y = map(int,input().split())
	adj[0][x].append(y)
	adj[1][y].append(x)

import sys
sys.setrecursionlimit(4*10**5+1)

def dfs(t,u): # Left, Right, Edges
	vis[t][u] = True

	ct = [0,0,0]
	ct[t] += 1
	for v in adj[t][u]:
		ct[2] += 1
		if not vis[t^1][v]:
			ctv = dfs(t^1,v)

			ct[0] += ctv[0]
			ct[1] += ctv[1]
			ct[2] += ctv[2]

	return ct

ans = 0
for u in range(1,MAX+1):
	if not vis[0][u]:
		L, R, M = dfs(0,u)
		ans += L*R-M//2

print(ans)
