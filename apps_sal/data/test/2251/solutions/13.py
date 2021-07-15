def dfs(p, f, gr, used):
	if p == f:
		return 1
	if used[p]:
		return 0
	used[p] = 1
	for v in gr[p]:
		if dfs(v, f, gr, used):
			return 1
	return 0

def check(gr, u, v):
	used = [0] * len(gr)
	return dfs(u, v, gr, used)

n, m = (int(x) for x in input().split())
cgr = [[[] for j in range(n)] for _ in range(m)]
for i in range(m):
	a, b, c = (int(x) for x in input().split())
	c -= 1
	a -= 1
	b -= 1
	cgr[c][a].append(b)
	cgr[c][b].append(a)
q = int(input())
for i in range(q):
	u, v = (int(x) for x in input().split())
	ans = 0
	for gr in cgr:
		ans += check(gr, u - 1, v - 1)
	print(ans)

