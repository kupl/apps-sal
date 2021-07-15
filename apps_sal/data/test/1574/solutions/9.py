V, E = tuple(int(i) for i in input().split())
adjList = [[] for i in range(V)]
degree = [0 for i in range(V)]
for i in range(E):
	u,v = tuple(int(i) for i in input().split())
	u-=1
	v-=1
	adjList[u].append(v)
	adjList[v].append(u)
	degree[u]+=1
	degree[v]+=1
	
ans = -1
for i in range(V):
	if(degree[i]<2):
		continue
	for n in range(len(adjList[i])):
		v1 = adjList[i][n]
		for m in range(len(adjList[v1])):
			v2 = adjList[v1][m]
			if(v2==i):
				continue
			if(not i in adjList[v2]):
				continue
			cost = max(degree[i]-2,0) + max(degree[v1]-2,0) + max(degree[v2]-2,0) 
			if(ans == -1 or ans>cost):
				ans = cost
print(ans)
