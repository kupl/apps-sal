from collections import deque
# from time import time

# tt = time()
n = int(input())
a = [0] + list(map(int, input().split()))
e = [[] for i in range(n + 1)]
for i in range(n - 1):
	u, v = list(map(int, input().split()))
	e[u].append(v)
	e[v].append(u)
# print(e)

# find all primes
isp = [1] * 501
prime = []
for i in range(2, 501):
	if isp[i]:
		prime.append(i)
	for p in prime:
		if i * p > 500:
			break
		isp[i * p] = 0
		if i % p == 0:
			break
lp = len(prime)

# gr is a forest, n is # of vertices
def diam(gr, n):
	vis = [0] * (n + 1)
	lvl = [-1] * (n + 1)
	maxlvl = 0
	for i in range(1, n + 1):
		if not vis[i]:
			q = deque([i])
			start = i
			while q:
				start = q.popleft()
				for to in gr[start]:
					if not vis[to]:
						vis[to] = 1
						q.append(to)
			q.append(start)
			# print(start)
			lvl[start] = 0
			tmplvl = 0
			while q:
				cur = q.popleft()
				for to in gr[cur]:
					if lvl[to] == -1:
						lvl[to] = lvl[cur] + 1
						q.append(to)
						tmplvl = lvl[to]
			maxlvl = max(maxlvl, tmplvl)
	return maxlvl + 1

# print('input', time() - tt)
# tt = time()

newn = [0] * (n + 1)
# find vertices in each graph
v = [[] for i in range(lp)]
other = {}
for i in range(1, n + 1):
	l = a[i]
	for j in range(lp):
		r = prime[j]
		if l % r == 0:
			v[j].append(i)
			while l % r == 0:
				l //= r
	if l != 1:
		if l in other:
			other[l].append(i)
		else:
			other[l] = [i]
for val in list(other.values()):
	v.append(val)
ans = 0
# build the graph
for i in range(len(v)):
	count = 1
	for node in v[i]:
		newn[node] = count
		count += 1
	if count == 1:
		continue
	g = [[] for i in range(count)]
	for node in v[i]:
		for to in e[node]:
			if newn[to]:
				g[newn[node]].append(newn[to])
	ans = max(ans, diam(g, count - 1))
	for node in v[i]:
		newn[node] = 0

print(ans)




