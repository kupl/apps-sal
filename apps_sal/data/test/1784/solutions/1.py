n, k = map(int, input().split())
a = list(map(int, input().split()))
mn = min(a)
if (max(a) - mn > k):
	print('NO')
else:
	print('YES')
	for i in range(n):
		arr = [1]*mn
		arr += [1+i for i in range(a[i]-mn)]
		print(' '.join(map(str, arr)))
