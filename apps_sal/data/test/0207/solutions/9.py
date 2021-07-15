n = int(input())
a = list(map(int, input().split()))
if n % 2:
	if a[0] % 2 and a[-1] % 2:
		print('Yes')
	else:
		print('No')
else:
	print('No')
