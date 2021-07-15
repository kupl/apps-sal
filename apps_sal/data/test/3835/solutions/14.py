from math import sqrt

n = int(input())

A = []

for i in range(n):
	A.append(list(map(int, input().split())))

ans = [0 for i in range(n)]

for i in range(n):
	x = A[i][(i + 1) % n] * A[(i + 1) % n][(i + 2) % n]

	x = x // (A[i][(i + 2) % n])

	ans[(i + 1) % n] = int(sqrt(x))


print(*ans)

