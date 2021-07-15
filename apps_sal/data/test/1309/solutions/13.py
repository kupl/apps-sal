n = int(input())

w = sorted(map(int, input().split()))
ans = 1e100
for i in range(2 * n):
	for j in range(i + 1, 2 * n):
		prev = -1
		s = 0
		for k in range(2 * n):
			if k == i or k == j:
				continue
			if prev == -1:
				prev = w[k]
			else:
				s += w[k] - prev
				prev = -1
		ans = min(ans, s)
print(ans)
