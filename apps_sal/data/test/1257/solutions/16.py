n,m=map(int,input().split())
a=[[0]*n for _ in range(n)]
for i in range(n*n):
	if i<(m-1)*n:
		a[i//(m-1)][i%(m-1)]=i+1
	else:
		a[(i-(m-1)*n)//(n-m+1)][(i-(m-1)*n)%(n-m+1)+m-1]=i+1
r=0
for j in range(n):
	r+=a[j][m-1]
print(r)
for i in range(n):
	for j in range(n):
		print(a[i][j],end=' ')
	print()
