(n, m), count, length = list(map(int, input().split())), {}, {}
for _ in range(m):
	a, b = list(map(int, input().split()))
	count[a] = count[a]+1 if a in count.keys() else 1
	length[a] = min(length[a], (b+n-a) % n) if a in length.keys() else (b+n-a) % n
for i in range(1, n+1):
		print(max((length[j] + j-i + n*(count[j]-(j >= i)) if count[j] != 0 else 0 for j in count.keys())), end=' ')
