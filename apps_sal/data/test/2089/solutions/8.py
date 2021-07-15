from collections import *
inf = int(1e9)

n, m, s, t = map(int, input().split())
a = [set() for _ in range(n+1)]
for _ in range(m):
	u, w = map(int, input().split())
	a[u].add(w)
	a[w].add(u)
	
# d1
d1 = [inf] * (n + 1)
q = deque([s])
d1[s] = 0
while q:
	i = q.popleft()
	d = d1[i]
	for j in a[i]:
		if d1[j] == inf:
			q.append(j)
			d1[j] = d + 1
			
# d2
d2 = [inf] * (n + 1)
q = deque([t])
d2[t] = 0
while q:
	i = q.popleft()
	d = d2[i]
	for j in a[i]:
		if d2[j] == inf:
			q.append(j)
			d2[j] = d + 1			

# calc
ans = 0
v = d1[t]
for i in range(1, n+1):
	for j in range(i+1, n+1):
		if i not in a[j]:
			v1 = d1[i] + 1 + d2[j]
			v2 = d1[j] + 1 + d2[i]
			if v1 >= v and v2 >= v:
				ans += 1
print(ans)	
