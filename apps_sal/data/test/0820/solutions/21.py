n = int(input())
m = int(input())
a = [0]*n
for i in range(n):
	a[i] = int(input())

a.sort(reverse=True)
for i in range(0, n):
	m -= a[i]
	if m <= 0:
		print(i+1)
		break

