n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
children = list(range(1, n + 1))

pos = 0
for i in range(k):
	pos = (pos + a[i]) % len(children)
	print(children[pos], end = ' ')
	del children[pos]
print()
