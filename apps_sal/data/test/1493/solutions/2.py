n,m = map(int, input().split())

a = []

for _ in range(n):
	tmp = []
	st = input()
	for i in st:
		if(i=='.'):
			tmp.append(1)
		else:
			tmp.append(0)
	a.append(tmp)

for i in range(n):
	tmp = ''
	for j in range(m):
		if(a[i][j]==1):
			if((i-j) % 2==0):
				tmp+='B'
			else:
				tmp+='W'
		else:
			tmp+='-'
	print(tmp)
