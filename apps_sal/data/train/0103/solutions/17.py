for nt in range(int(input())):
	n,m = map(int,input().split())
	mat = []
	for i in range(n):
		mat.append(list(map(int,input().split())))
	row = {}
	col = {}
	for i in range(n):
		if 1 in mat[i]:
			row[i]=1
	for i in range(m):
		flag = 0
		for j in range(n):
			if mat[j][i]==1:
				flag = 1
				break
		if flag:
			col[i]=1
	count = 0
	for i in range(n):
		for j in range(m):
			if i not in row and j not in col:
				row[i]=1
				col[j]=1
				count+=1
	if count%2:
		print ("Ashish")
	else:
		print ("Vivek")
