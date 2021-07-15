n = int(input())
a = [int(input()) for i in range(n)]
for i in range(2 ** n):
	su = 0
	for j in range(n):
		if ((1 << j) | i) != i:
			su += a[j]
		else:
			su -= a[j]
	if su % 360 == 0:
		print('YES')
		return
print('NO')
