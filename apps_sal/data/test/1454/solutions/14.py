__author__ = 'Esfandiar'
n,m = list(map(int,input().split()))
a = list()
for i in range(n):
	a.append(list(map(int,input().split())))
su = 0
M = -1
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if a[i][j] == 0:
            M = a[i][j+1] - 1
            M = min(M,a[i+1][j] - 1)
            a[i][j] = M
        su+=a[i][j]

for i in range(n):
	for j in range(m-1):
		if a[i][j] >= a[i][j+1]:
			print(-1)
			return

for i in range(m):
	for j in range(n-1):
		if a[j][i] >= a[j+1][i]:
			print(-1)
			return
print(su)


