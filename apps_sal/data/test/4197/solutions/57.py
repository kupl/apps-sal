n = int(input())
a = list(map(int, input().split()))
a = {a[i-1]: i for i in range(1, n+1)}
for x in sorted(a.items()):
	print(x[1], end=' ')
