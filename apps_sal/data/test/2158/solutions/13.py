# maa chudaaye duniya
from collections import defaultdict
graph = defaultdict(list)
n = int(input())
weights = {}
for _ in range(n-1):
	a, b, w = map(int, input().split())
	edge1 = '{} : {}'.format(a, b)
	edge2 = '{} : {}'.format(b, a)
	graph[a].append(b)
	graph[b].append(a)
	weights[edge1] = w
	weights[edge2] = w

maxsf = [-10**9]
visited = [False for i in range(n+1)]

def dfs(node, parent, dist):
	visited[node] = True
	# print(maxsf)
	# print('checking ', node, parent)
	# print(visited)
	if parent != -1:
		e ='{} : {}'.format(parent, node)
		e1 = '{} : {}'.format(node, parent)
		if e in weights:
			dist += weights[e]
			# print(e, dist)
		else:
			dist += weights[e1]
			# print(e1, dist)
		if dist > maxsf[0]:
			maxsf[0] = dist
	for children in graph[node]:
		if not visited[children]:
			dfs(children, node, dist)
	
dfs(0, -1, 0)
print(*maxsf)
