n = int(input())
m = n // 2 + 1
print(m)
for i in range(1, n // 2 + 1):
	print(1, i)
M = 1
for i in range(n // 2 + 1, n + 1):
	print(m, M)
	M += 1
