path = []
n = int(input())
for it in range(0, n):
	data = list(map(int, input().split(' ')))
	if data[0] == 1:
		path.append(data[1:])
	else:
		vis = [False] * (len(path) + 1)
		que = [data[1] - 1]
		while len(que):
			p = que[0]
			del que[0]
			for i, v in enumerate(path):
				if (v[0] < path[p][0] < v[1] or v[0] < path[p][1] < v[1]) and not vis[i]:
					vis[i] = True
					que.append(i)
		print('YES' if vis[data[2] -1] else 'NO')

