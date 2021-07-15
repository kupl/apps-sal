n = int(input())
arr = [int(i) for i in input().split()]

sor = [[arr[i], n - i] for i in range(n)]
sor.sort()

m = int(input())

for i in range(m):
	op = []
	[q, index] = [int(i) for i in input().split()]
	for j in range(q):
		op.append(n - sor[-1-j][1])
	op.sort()
	print(arr[op[index - 1]])

