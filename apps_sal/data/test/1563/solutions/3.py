3
# D. Colorful Graph
from collections import deque

MAX_COLORS = 10 

def bfs(vertex):
	nonlocal adjlist, visited, colors, dvt, count, idx
	queue = deque()
	queue.append(vertex)
	visited[vertex] = 1
	while queue:
		curv = queue.popleft()
		for v in adjlist[curv]:
			if colors[v] != colors[curv]:
				if colors[curv] not in dvt:
					dvt[colors[curv]] = {colors[v]}
				else:
					dvt[colors[curv]].add(colors[v])
				if len(dvt[colors[curv]]) > count:
					idx = colors[curv]
					count = len(dvt[colors[curv]])
				elif len(dvt[colors[curv]]) == count and colors[curv] < idx:
					idx = colors[curv]
			if visited[v] == 0:
				queue.append(v)
				visited[v] = 1

n, m = [int(x) for x in input().split()]
colors = []
adjlist = [[] for x in range(n)]
dvt = {} 
visited = [0] * n
colors = [int(x) for x in input().split()]
for i in range(m):
	x, y = [int(x) for x in input().split()]
	x -= 1
	y -= 1
	adjlist[x].append(y)
	adjlist[y].append(x)

count = 0
idx = min(colors)
for i in range(n):
	if visited[i] == 0:
		bfs(i)

print(idx)

