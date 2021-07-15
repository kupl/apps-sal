import sys
import math
from collections import defaultdict,deque
import heapq
def find(node,parent):
	while parent[node]!=node:
		node=parent[node]
	return node
def union(a,b,child,parent):
	#print(a,'a',b,'b')
	para=find(a,parent)
	parb=find(b,parent)
	#print(para,'para')
	ca=child[para]
	cb=child[parb]
	if para!=parb:
		if ca>cb:
			parent[parb]=para
			child[para]+=child[parb]
		else:
			parent[para]=parb
			child[parb]+=child[para]
		
n,m,d=map(int,sys.stdin.readline().split())
graph=defaultdict(list)
parent=[i for i in range(n+1)]
child=[1 for i in range(n+1)]
edges=[]
for i in range(m):
	u,v=map(int,sys.stdin.readline().split())
	graph[u].append(v)
	graph[v].append(u)
	#edges.append([u,v])
vis=defaultdict(int)
q=deque()

vis[1]=1
for j in graph[1]:
	if vis[j]==0:
		vis[j]=1
		q.append(j)
		#print(j,'j')
		child[j]+=1
		#print(child[j],'child')
		while q:
			cur=q.pop()
			#print(cur,'cur')
			for i in graph[cur]:
				if vis[i]==0:
					q.append(i)
					if cur!=1 and i!=1:
						#print(cur,'cur',i,'i')
						union(cur,i,child,parent)
					vis[i]=1
if len(graph[1]) < d:
	print("NO")
	return
#print(graph[1],'one')
#print(parent,'parent')
#print(child,'child')
cnt=set()
for i in graph[1]:
	cnt.add(find(i,parent))
#print(cnt,'cnt')
if len(cnt)>d:
	print("NO")
	return
q=deque()
res=0
ans=[]
vis=defaultdict(int)
for i in cnt:
	ans.append([1,i])
	q.append(i)
	vis[i]=1
	res+=1
rem=d-res
vis[1]=1
for i in graph[1]:
	if rem>0 and vis[i]==0:
		vis[i]=1
		q.append(i)
		rem-=1
		ans.append([1,i])

while q:
	cur=q.popleft()
	for j in graph[cur]:
		if vis[j]==0:
			q.append(j)
			ans.append([cur,j])
			vis[j]=1
print("YES")
for i in range(n-1):
	print(ans[i][0],ans[i][1])
