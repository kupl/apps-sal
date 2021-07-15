import sys
def input():
	return sys.stdin.readline()[:-1]

n = int(input())
adj = [[] for _ in range(n)]
for i in range(n-1):
	u, v = map(int, input().split())
	adj[u-1].append((v-1, i))
	adj[v-1].append((u-1, i))

if max([len(x) for x in adj]) <= 2:
	print(*list(range(n-1)), sep="\n")
else:
	ans = [-1 for _ in range(n-1)]
	for i in range(n):
		if len(adj[i]) > 2:
			ans[adj[i][0][1]] = 0
			ans[adj[i][1][1]] = 1
			ans[adj[i][2][1]] = 2
			break
	tmp = 3
	for i in range(n-1):
		if ans[i] < 0:
			ans[i] = tmp
			tmp += 1
	print(*ans, sep="\n")

