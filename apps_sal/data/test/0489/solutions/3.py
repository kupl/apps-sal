n = int(input())
a = list(map(int, input().split()))
a.sort()
x = a[0]
y = a[1]
z = a[2]
if x < y and y < z:
	print(a.count(z))
elif x < y and y == z:
	t = a.count(y)
	print(t * (t - 1) // 2)
elif x == y and y < z:
	print(a.count(z))
else:
	t = a.count(x)
	print(t * (t - 1) * (t - 2) // 6)

