n,q=list(map(int,input().split()))
from heapq import heappush as pu
from heapq import heappop as po
from bisect import bisect_right as br 

tr=[[] for i in range(n)]
size=[1 for i in range(n)]

p=list(map(int,input().split()))
p=[i-1 for i in p]

for i in range(n-1):
	tr[p[i]].append(i+1)
for i in range(n):
	tr[i].sort(reverse=True)

h={}
h[0]=0
s=[0]
m=[]
while s:
	x=s.pop()
	m.append(x)
	for i in tr[x]:
		s.append(i)
		h[i]=h[x]+1

d=[(i,h[i]) for i in range(n)]
d.sort(key=lambda x:x[1])
d=[i[0] for i in d]

for i in range(n-1,0,-1):
	size[p[d[i]-1]]+=size[d[i]]
ind={}
for i in range(n):
	ind[m[i]]=i
for _ in range(q):
	u,k=list(map(int,input().split()))
	u-=1
	if k>size[u]:
		print(-1)
	else:
		i=ind[u]
		print(m[i+k-1]+1)

