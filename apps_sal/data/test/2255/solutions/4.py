from heapq import *

n, m = list(map(int, input().split()))
vis = [0, 1] + [0] * (n - 1)
e = [[] for i in range(n + 1)]
for i in range(m):
	u, v = list(map(int, input().split()))
	e[u].append(v)
	e[v].append(u)
ans = []
h = [1]
while h:
	cur = heappop(h)
	ans.append(cur)
	for to in e[cur]:
		if not vis[to]:
			vis[to] = 1
			heappush(h, to)
print(*ans)


