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
			# print(stack, flag)
			# print(sol)
		if(flag):
			rem = 0
			tree_size = 1
			for item in adj[i]:
				if(item==parent):
					continue
				subtree_size,t = sol[item]
				# print(item, subtree_size, t)
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
	u,v = list(map(int,input().split()))
	adj[u].append(v)
	adj[v].append(u)
if(n%2==1):
	print(-1)
else:
	ans = dfs_new(adj,n)
	print(ans)

