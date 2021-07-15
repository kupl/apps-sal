n =int(input())
W = []
A = []
B = []

for i in range(n):
	a = list(map(int,input().split()))
	W.append(a)
	A.append([0]*n)
	B.append([0]*n)

	
for i in range(n):
		for j in range(n):
			if i!=j:
				A[i][j] = (W[i][j]+W[j][i])/2
				B[i][j] = (W[i][j]-A[i][j])
			else:
				A[i][j] = W[i][j]

for i in range(n):
	for j in range(n):
		print(A[i][j],end = " ")
	print()

for i in range(n):
	for j in range(n):
		print(B[i][j],end = " ")
	print()
