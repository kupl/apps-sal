from collections import deque

n,m=map(int,input().split())
a=list(map(int,input().split()))
tree={}
for i in range(n-1):
	x,y=map(int, input().split())
	if x not in tree:
		tree[x]=[]
	if y not in tree:
		tree[y]=[]
	tree[x].append(y)
	tree[y].append(x)

#BFS
res=0
root=(1,a[0],0) #node,sum,from
d=deque() 
d.append(root)
while len(d)!=0:
	curr=d.popleft()
	children=tree[curr[0]]
	if len(children)==1 and curr[0]!=1: #leaf with only father, not root
		res+=1
	else:
		for child in children:
			if child==curr[2]: #father
				continue
			next_sum=0
			if a[child-1]==1:
				next_sum=curr[1]+a[child-1]
				if next_sum>m:
					continue
			
			to_add=(child,next_sum,curr[0])
			d.append(to_add)

print(res)
