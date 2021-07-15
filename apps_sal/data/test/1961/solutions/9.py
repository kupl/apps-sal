def mi():
	return list(map(int, input().split()))

'''
5 7
.......
.#####.
.#.#.#.
.#####.
.......
'''
n,m = mi()
a = [0]*n
b = [0]*n
for i in range(n):
	a[i] = list(input())
	b[i] = a[i].copy()
for i in range(n-2):
	for j in range(m-2):
		if a[i][j]=='#' and a[i+1][j]=='#' and a[i+2][j]=='#' and a[i+2][j+1]=='#' and a[i+2][j+2]=='#' and a[i+1][j+2]=='#' and a[i][j+2]=='#' and a[i][j+1]=='#':
			b[i][j]=b[i+1][j]=b[i+2][j]=b[i+2][j+1]=b[i+2][j+2]=b[i+1][j+2]=b[i][j+2]=b[i][j+1]='.'
for i in range(n):
	for j in range(m):
		if b[i][j]=='#':
			print ('NO')
			return
print ('YES')

