n = int(input())
a = list(map(int, input().split()))
p = n // 2
t = p % 2
for i in range(t, len(a) // 2, 2):
	a[i], a[n - i - 1] = a[n - i - 1], a[i]
if n // 2 % 2:
	a = a[::-1]
for i in a:
	print(i, end = ' ')
