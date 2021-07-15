n = int(input())
m = n // 2 + 1
print(m)
a = 1
b = 1
for i in range(n):
	print(a, b)
	if a < m:
		a += 1
	else:
		b += 1
