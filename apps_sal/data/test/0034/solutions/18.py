n, a, b = list(map(int,input().split()))
z = []
for i in range(1, n):
	z += [min(a // i, b // (n - i))]
print(max(z))

