n,k = list(map(int,input().split()))
p = [ [0 for j in range(n)] for j in range(n)]
for i in range(n):
	p[i][i] = k
for i in range(n):
	print(*p[i])

