def rotate_r(ar, row, n):
	ar[row] = ar[row][-n:] + ar[row][:-n]
	return ar

def rotate_c(ar, m, col):
	#c = ar[col][0]
	c = ar[m - 1][col]
	for i in range(m - 1, 0, -1):
	#for i in range(m - 1):
		ar[i][col] = ar[i - 1][col]
	#ar[col][m - 1] = c
	ar[0][col] = c
	return ar

def print_matr(ar, n):
	for i in range(n):
		print(*ar[i])		

ar2 = []	

n, m, q = list(map(int, input().split()))
#for i in range(n):
#	ar = list(map(int, input().split()))
#	ar2.append(ar)


query = [0 for i in range(q)]
rows = [0 for i in range(q)]
cols = [0 for i in range(q)]
nums = [0 for i in range(q)]

for i in range(q):
	ar = list(map(int, input().split()))
	query[i] = ar[0]
	if ar[0] == 3:
		rows[i] = ar[1] - 1
		cols[i] = ar[2] - 1
		nums[i] = ar[3]
	elif ar[0] == 1:
		rows[i] = ar[1] - 1
	else:
		cols[i] = ar[1] - 1

#print(query)
ans = [[0] * m for i in range(n)]

for i in range(q - 1, -1, -1):
	if query[i] == 3:
		ans[rows[i]][cols[i]] = nums[i]
		#print('\n')
		#print_matr(ans, n)
		#print("l", rows[i] + 1, cols[i] + 1)
		#print(i, nums[i])
	elif query[i] == 1:
		ans = rotate_r(ans, rows[i], 1)
		#print('\n')
		#print_matr(ans, n)
	else:
		ans = rotate_c(ans, n, cols[i])
		#print('\n')
		#print_matr(ans, n)

#row, n = map(int, input().split())

#print(rotate_r(ar2, 0, n))
print_matr(ans, n)
#ans = rotate_c(ans, n, 0)
#print_matr(ans, n)

