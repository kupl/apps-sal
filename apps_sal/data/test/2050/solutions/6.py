n, k = map(int, input().split())
print(k * (2 * (3 * n) - 1))
now = 1
m = 2
for i in range(n):
	print(k * m, end = ' ')
	for j in range(3):
		print(k * now, end = ' ')
		now += 2
	m += 6
	print()
