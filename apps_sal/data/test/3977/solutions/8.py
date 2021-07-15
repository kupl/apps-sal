from collections import Counter as cntr
from math import inf
def cin():
	return map(int, input().split(' '))
def dfs(graph, src):
	nonlocal visited, cnt
	cnt += 1
	for v in graph[src]:
		if visited[v] == False:
			visited[v] = True
			dfs(graph, v)
	return cnt

n,m,k = cin()
govs = list(cin())
hong = {i:[] for i in range(n)}
for i in range(m):
	u, v = cin()
	u -= 1
	v -= 1
	hong[u].append(v)
	hong[v].append(u)


visited = [False for i in range(n)]
count = []
for gov in govs:
	gov -= 1
	visited[gov] = True
	cnt = 0
	count.append(dfs(hong, gov))



count = sorted(count)
for i in range(n):
	if visited[i] == False:
		visited[i] = True
		cnt = 0
		count[-1]+=dfs(hong, i)
su = 0
for i in count:
	su += i*(i-1)//2
print(su-m)
