n = int(input())
f = [-1] + list(map(int, input().split()))
g = [-1]*(n+1)
h = [-1]
c = 1
for i in range(1, n+1):
	if(f[i] == i):
		g[i] = c
		h += [i]
		c += 1

hinv = {}
m = len(h)-1
for i in range(1, m+1):
	hinv[h[i]] = i

for i in range(1, n+1):
	if(g[i] == -1):
		try:
			g[i] = hinv[f[i]]
		except:
			print(-1)
			return
print(m)
print(*g[1:])
print(*h[1:])
