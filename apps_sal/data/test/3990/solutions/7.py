n, m = list(map(int, input().split()))
dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
level = [-1 for i in range(n + 1)]
stack = []

def bfs(src, lvl, flag):
	level[src] = lvl
	stack.append(src)
	p = 0
	while True:
		for i in range(1, n + 1):
			if dp[src][i] == flag:
				#print (i, i)
				if level[i] == -1:
				#	print (i, i)
					stack.append(i)
					level[i] = level[src] + 1
		if len(stack) <= p + 1:
			break
		p += 1
		#print (stack)
		src = stack[p]
		if src == n:
			return level[src]
			break
	return -1

for i in range(m):
	a, b = list(map(int, input().split()))
	dp[a][b] = 1
	dp[b][a] = 1
	
if dp[1][n]:
	print(bfs(1, 0, 0))
	
else:
	print(bfs(1, 0, 1))

