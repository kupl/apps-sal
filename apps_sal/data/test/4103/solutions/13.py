n, b, a = list(map(int, input().split()))
l = list(map(int, input().split()))
aa = a
for i in range(n):
	if a == 0 and b == 0:
		print(i)
		break
	if l[i] == 0:
		if a > 0:
			a -= 1
		else:
			b -= 1
	if l[i] == 1:
		if a == aa:
			a -= 1
		else:
			if b > 0:
				b -= 1
				a = min(aa, a + 1)
			else:
				a -= 1
	if i == n - 1:
		print(n)
