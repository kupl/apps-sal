def dfs(adj,i,parent):
	rem = 0
	tree_size = 1
	for item in adj[i]:
		if(item==parent):
			continue
		subtree_size,t = dfs(adj,item,i)
		rem += t
		if(subtree_size%2==0):
			rem +=1
		tree_size += subtree_size
	return (tree_size,rem)

def dfs_new(adj,n):
	stack = [(1,0)]
	sol = [None for i in range(n+1)]
	while(not len(stack)==0):
		i,parent = stack[-1]
		flag = True
		for item in adj[i]:
			if(item==parent):
				continue
			if(sol[item]==None):
				stack.append((item,i))
				flag = False
		if(flag):
			rem = 0
			tree_size = 1
			for item in adj[i]:
				if(item==parent):
					continue
				subtree_size,t = sol[item]
				if(subtree_size%2==0):
					rem+=1
				rem += t
				tree_size += subtree_size
			sol[i] = [tree_size,rem]
			stack.pop(-1)
	# print(sol)
	return sol[1][1]


n = int(input())
adj = [[] for i in range(n+1)]
for _ in range(n-1):
	u,v = map(int,input().split())
	adj[u].append(v)
	adj[v].append(u)
if(n%2==1):
	print(-1)
else:
	ans = dfs_new(adj,n)
	print(ans)
