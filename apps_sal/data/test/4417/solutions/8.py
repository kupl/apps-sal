q = int(input())

for request in range(q):
	n, k = list(map(int, input().split()))
	a = list(map(int, input().split()))

	b = min(a) + k
	if max(a) > b + k:
		print(-1)
	else:
		print(b)

