from collections import defaultdict as dd
g=dd(list)
def addE(u,v):
	g[u].append(v)
	g[v].append(u)
n=int(input())
l=[int(x) for x in input().split()]
for i in range(n):
	addE(i+1,l[i])
visited=[False]*(n+1)
def dfs(v,count):
	visited[v]=True
	stack=[v]
	while len(stack)!=0:
		cur=stack.pop()
		for ch in g[cur]:
			if visited[ch]:
				continue
			visited[ch]=True
			count+=1
			stack.append(ch)
	return count

ans=[]
for i in range(1,n+1):
	if not visited[i]:
		ans.append(dfs(i,1))

ans=sorted(ans,reverse=True)
if  len(ans) ==1:
	print(ans[0]*ans[0])
else:
	ans[1]+=ans[0]
	ans.pop(0)
	print(sum(x*x for x in ans))




