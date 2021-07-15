from collections import defaultdict

n,x,y = list(map(int,input().split()))
graph = defaultdict(list)
vis = [False for i in range(n+1)]
mat = [False for i in range(n+1)]
subtree = [0 for i in range(n+1)]

for i in range(n-1):
	u,v = list(map(int,input().split()))
	graph[u].append(v)
	graph[v].append(u)
q = []
cur = 0
for v in graph[x]:
	if v!=y:
		q.append([v,v])
	else:
		cur = v
vis[x] = 1
while q!=[]:
	temp = q.pop()
	u,v = temp
	vis[u] = True
	subtree[v]+=1
	for node in graph[u]:
		if vis[node]==False:
			if node!=y:
				q.append([node,v])
			else:
				cur = v
val = sum(subtree)
val1 = (val+1-subtree[cur])
val2 = n-(sum(subtree)+1)
val = val1*val2
print(n*(n-1)-val)
