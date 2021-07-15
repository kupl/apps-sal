n,m,k = list(map(int,input().split()))
graph = {}
vertices = set()
ans = -1
floor = [False] * (n+1)
for i in range(m):
	u,v,l = list(map(int,input().split()))
	if u not in vertices : 
		vertices.update([u])
		graph[u] = []
	if v not in vertices : 
		vertices.update([v])
		graph[v] = []
	graph[u].append([v,l])
	graph[v].append([u,l])
if k!= 0 :
	A = []
	for i in input().split():
		floor[int(i)] = True
		A.append(int(i))
	valids = []
	for x in A:
		if x in vertices:
			for nb in graph[x]:
				if not floor[nb[0]]:
					valids.append(nb[1])
	if len(valids)>0 :
		ans = min(valids)

print(ans)



