from collections import Counter

n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
d = Counter(c.values())

dx = [0 for _ in range(n+1)]
for i in range(1, n+1):
	dx[i] = dx[i-1] + i*d[i]

xdx = [0 for _ in range(n+2)]
xdx[n] = d[n]
for i in range(n-1, 0, -1):
	xdx[i] = xdx[i+1] + d[i]

res = [0] + [(dx[i] + i*xdx[i+1]) // i for i in range(1, n+1)]
ans = [0 for _ in range(n)]
cur = n
for i in range(n):
	while cur > 0 and res[cur] < i+1:
		cur -= 1
	if cur > 0:
		ans[i] = cur
print(*ans, sep="\n")
