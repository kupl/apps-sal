import sys
input=sys.stdin.readline
from collections import defaultdict
def dfs(i):
	st=[i]
	while st:
		x=st.pop()
		if vis[x]:continue
		vis[x]=1
		for v in sorted(g[x]):
			if c[x-1]!=c[v-1]:d[c[x-1]].add(c[v-1])
			if not vis[v]:
				st.append(v)

n,m=map(int,input().split())
c=list(map(int,input().split()))
g=[[] for i in range(n+1)]
for i in range(m):
	x,y=map(int,input().split())
	g[x].append(y)
	g[y].append(x)
d=defaultdict(set)
vis=[0]*(n+1)
for i in range(1,n+1):
	if vis[i] == 0:
		dfs(i)
k=sorted(d.keys(),key=lambda i:(len(d[i]),-i))
if not k:print(min(c))
else:print(k[-1])
