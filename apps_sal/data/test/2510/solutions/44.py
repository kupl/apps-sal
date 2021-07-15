def root(a):
	if p[a] == a:
		return a
	p[a] = root(p[a])
	return p[a]

def merge(a, b, p, size):
	ra = root(a)
	rb = root(b)
	if ra == rb:
		return
	size[rb] += size[ra]
	p[ra] = rb

n,m = list(map(int, input().split()))

size = [1]*n
p = [0]*n
for i in range(n):
	p[i] = i

for i in range(m):
	a,b = list(map(int, input().split()))
	a -= 1
	b -= 1
	merge(a,b,p,size)

ans = 0
for x in size:
	ans = max(ans, x)

print(ans)

