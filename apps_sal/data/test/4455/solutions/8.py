

def solve(n,m,a,adj):
	a = sorted(a)

	res = []
	for i in range(n):
		res.append(0)

	equal = 0
	for i in range(n):
		pos = a[i][1]
		if (i == 0):
			res[pos] = 0
			continue

		if (a[i][0] == a[i-1][0]):
			equal += 1
		else:
			equal = 0

		res[pos] = i - equal - len(adj[pos])

	for i in res:
		print(i, end = ' ')
		





n, m = map(int, input().split())

tmp = list(map(int, input().split()))
a = []
adj = []
for i in range(n):
	a.append((tmp[i],i))
	adj.append([])


for i in range(m):
	x, y = map(int, input().split())
	x -= 1
	y -= 1
	if (a[x][0] < a[y][0]):
		adj[y].append(x)
	elif (a[x][0] > a[y][0]):
		adj[x].append(y)
	

solve(n,m,a,adj)
