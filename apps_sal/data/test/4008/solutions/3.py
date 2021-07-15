n, k = list(map(int, input().split()))

a = list(map(int, input().split()))

b = [[False for j in range(k + 1)] for i in range(5010)]

ans = [0 for _ in range(n)]

for i in range(k):
	b[a[i]][i + 1] = True
	ans[i] = i + 1

for i in range(k, n):
	for j in range(1, k + 1):
		if not b[a[i]][j]:
			b[a[i]][j] = True
			ans[i] = j
			break

if min(ans) == 0:
	print('NO')
else:
	print('YES')
	print(*ans)

