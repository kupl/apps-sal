n=int(input())
graph=[[] for i in range(n)]
for i in range(n-1):
	x,y=map(int,input().split())
	graph[x-1].append(y)
	graph[y-1].append(x)
c=0
for i in range(n):
	if len(graph[i])==1:
		c+=1
print(c)
