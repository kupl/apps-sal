n=int(input())
a=[]
for i in range(n):
	a.append(list(map(int,input().split())))
for i in range(n):
	for j in range(n):
		c=0
		if a[i][j]==1:
			continue
		for k in range(n):
			for l in range(n):
				if a[i][j]==a[i][k]+a[l][j]:
					c=1
					break
			if c:
				break
		if not c:
			print('No')
			return
print('Yes')

