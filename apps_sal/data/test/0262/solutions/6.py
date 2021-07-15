n = int(input()) 
if n == 1:
	print('1')
	return
A = []
C = [0 for i in range(n)]
diag1 = 0
diag2 = 0
for i in range(n):
	B = list(map(int, input().split()))
	for j in range(n):
		el = B[j]
		C[j] += el
		if i == j:
			diag1 += el
		if i + j == n - 1:
			diag2 += el	
		if el == 0:
			x = i
			y = j
	A.append(B)
if x == 0:
	s = sum(A[1])
else:
	s = sum(A[0])	
for i in range(n):
	if i != x:
		if s != sum(A[i]):
			print('-1')
			return
for i in range(n):
	if i != y:
		if s != C[i]:
			print('-1')
			return
ans = s - C[y]
if ans + sum(A[x]) != s:
	print('-1')
	return
if x == y:
	diag1 += ans
if x + y == n - 1:
	diag2 += ans
if diag1 != s:
	print('-1')
	return
if diag2 != s:
	print('-1')
	return							
if ans < 1:
	print('-1')
	return
print(ans)

