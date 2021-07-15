#!/usr/bin/env python
from collections import deque

n, m = list(map(int, input().split()))
g = [[] for _ in range(n)]
e = []
for _ in range(m):
	u, v = [int(_) - 1 for _ in input().split()]
	e.append((u, v))
	g[u].append(v); g[v].append(u)

p = [-1 for _ in range(n)]
p[0] = True
ok = True
q = deque([0])
while q:
	f = q.popleft()
	for t in g[f]:
		if p[t] == -1:
			q.append(t)
			p[t] = not p[f]
		elif p[t] == p[f]:
			ok = False

if not ok:
	print('NO')
else:
	print('YES')
	print(''.join(('1' if p[e[i][0]] else '0') for i in range(m)))

