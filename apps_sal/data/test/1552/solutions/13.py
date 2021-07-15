n = int(input())
A = [[] for i in range(3)]
X = list(map(int, input().split()))
for i in range(n):
	A[X[i] - 1].append(i + 1)
Min = min(len(A[0]), len(A[1]), len(A[2]))
print(Min)
for i in range(Min):
	print(A[0][i], A[1][i], A[2][i])

