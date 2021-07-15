n = int(input())
arr = {}
mi = 0
ma = 0
t, i = input().split()
arr[i] = 0
for _ in range(n-1):
	t, i = input().split()
	if t == 'L':
		mi -= 1
		arr[i] = mi
	elif t == 'R':
		ma += 1
		arr[i] = ma
	else:
		print(min(ma-arr[i], arr[i]-mi))

