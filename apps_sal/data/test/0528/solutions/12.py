from collections import Counter as cntr
from math import inf
def cin():
	return list(map(int, input().split(' ')))
def dfs(graph, src, n):
	q = [src]
	h = 0
	nonlocal visited
	edges = 0
	while q:
		idx = q.pop()
		h += 1

		for v in graph[idx]:
			edges += 1
			if visited[v] == False:
				visited[v] = True
				q.append(v)
	return h,edges
n,m = cin()
g = {i:[] for i in range(n)}
for i in range(m):
	a, b = cin()
	a -= 1
	b -= 1
	g[a].append(b)
	g[b].append(a)
visited = [False for i in range(n)]
for i in range(n):
	if visited[i] == False:
		visited[i] = True
		v,e = dfs(g, i, n)
		e = e//2

		if e != (v*(v-1))//2:
			print('NO')
			return
print('YES')



