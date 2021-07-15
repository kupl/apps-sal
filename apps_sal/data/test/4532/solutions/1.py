t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	b = [(k-a[i]%k)%k for i in range(n)]
	mx = {}
	mx[0] = -1
	for x in b:
		if x == 0:
			continue
		if x not in mx:
			mx[x] = x
		else:
			mx[x] += k

	print(max(mx.values())+1)
