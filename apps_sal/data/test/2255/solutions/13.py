import bisect

def dfs(i,vis,g):
	print(i,end=" ")
	vis[i]=1
	for j in g[i]:
		if vis[j]==0:
			dfs(j,vis,g)

n,m=map(int,input().split())
g=[[] for i in range(n+1)]
for i in range(m):
	u,v=map(int,input().split())
	bisect.insort(g[u],v)
	bisect.insort(g[v],u)
bfs=[1]
l=1
vis=[0]*(n+1)
vis[1]=1
while l!=0:
	i=bfs.pop(0)
	print(i,end=" ")
	l-=1
	for j in g[i]:
		if vis[j]==0:
			bisect.insort(bfs,j)
			vis[j]=1
			l+=1

#dfs(1,vis,g)
print()

