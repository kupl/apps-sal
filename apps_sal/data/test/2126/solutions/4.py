n,m,h = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
	for j in range(m):
		if c[i][j] == 1:
			c[i][j] = min(a[j],b[i])

for i in range(n):
	print(*c[i])
