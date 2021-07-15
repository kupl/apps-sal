n,m = list(map(int,input().split()))
inp = [input() for _ in range(n) ]
mat = [[] for _ in range(m) ]
for row in inp:
	r = row.split()
	for idx,val in enumerate(r):
		mat[idx].append(int(val))
def valid(row):
	count = 0
	for idx,col in enumerate(mat):
		if (idx + 1) != col[row]:
			count += 1
			if count > 2:
				return False
	return count <= 2

def try_swap(col1,col2):
	temp = mat[col1]
	mat[col1] = mat[col2]
	mat[col2] = temp
	for row in range(n):
		if not valid(row):
			temp = mat[col2]
			mat[col2] = mat[col1]
			mat[col1] = temp
			return False
	temp = mat[col2]
	mat[col2] = mat[col1]
	mat[col1] = temp
	return True

for col in range(m):
	for col2 in range(col + 1,m):
		if try_swap(col,col2):
			print('YES')
			import sys
			return
if try_swap(0,0):
	print('YES')
else:
	print('NO')

