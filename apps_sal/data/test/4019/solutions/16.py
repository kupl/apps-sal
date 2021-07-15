import collections as cc
import math as mt
import sys
I=lambda:list(map(int,input().split()))
def find(u):
	while u!=parent[u]:
		u=parent[u]
	return u
def union(u,v):
	a=find(u)
	b=find(v)
	if a!=b:
		parent[a]=parent[b]=min(a,b)
n,m,d=I()
uu=set()
uu.add(1)
parent=[i for i in range(n+1)]
g=cc.defaultdict(list)
on=[]
tf=cc.defaultdict(int)
other=[]
for i in range(m):
	x,y=sorted(I())
	g[x].append(y)
	g[y].append(x)
	if x!=1 and y!=1:
		other.append([x,y])
		union(x,y)
temp=g[1]
con=[find(i) for i in set(temp)]
if len(set(con))>d or len(set(temp))<d:
	print("NO")
	return
else:
	print("YES")
	used=cc.defaultdict(int)
	ans=[]
	st=cc.deque()
	use=[0]*(n+1)
	use[1]=1
	j=0
	for i in range(len(temp)):
		if not used[find(temp[i])]:
			used[find(temp[i])]=1
			ans.append([1,temp[i]])
			st.append(temp[i])
			use[temp[i]]=1
			d-=1
	for i in range(d):
		while use[temp[j]]==1:
			j+=1
		ans.append([1,temp[j]])
		st.append(temp[j])
		use[temp[j]]=1
	while st:
		x=st.popleft()
		use[x]=1
		for y in g[x]:
			if not use[y]:
				ans.append([x,y])
				st.append(y)
				use[y]=1
	for i in ans:
		print(*i)

