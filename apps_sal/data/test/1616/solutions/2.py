import sys

MAX = 1_000_005
lp = [0] * MAX
pr = []
pid = {1: 0}
for i in range(2, MAX):
	if not lp[i]:
		lp[i] = i
		pr.append(i)
		pid[i] = len(pr)
	for p in pr:
		if p > lp[i] or i * p >= MAX:
			break
		lp[i * p] = p

n = int(input())
a = list(map(int, input().split()))

g = [[] for _ in range(len(pid))]
e = set()
for x in a:
	f = []
	while x > 1:
		p, c = lp[x], 0
		while lp[x] == p:
			x //= p
			c ^= 1
		if c:
			f.append(p)
	if not f:
		print(1)
		return
	f += [1] * (2 - len(f))
	u, v = pid[f[0]], pid[f[1]]
	if (u, v) in e or (v, u) in e:
		print(2)
		return
	g[u].append(v)
	g[v].append(u)

def bfs(s):
	d = [-1] * len(pid)
	d[s] = 0
	q = [(s, -1)]
	while q:
		q2 = []
		for u, p in q:
			for v in g[u]:
				if d[v] != -1:
					if v != p:
						return d[u] + d[v] + 1
				else:
					d[v] = d[u] + 1
					q2.append((v, u))
		q = q2

ans = n + 1
for i in range(len(pid)):
	if i > 0 and pr[i - 1] ** 2 >= MAX:
		break
	ans = min(ans, bfs(i) or ans)
print(ans if ans <= n else -1)

