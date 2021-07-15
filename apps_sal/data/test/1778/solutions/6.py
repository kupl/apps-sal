n = int(input())
a = list(map(int, input().split()))
a = [(a[i], 0) for i in range(n)]
b = list(map(int, input().split()))
b = [(b[i], 1) for i in range(n)]
ab = sorted(a + b, key=lambda x: x[0], reverse=True)
ans = 0
for i in range(2 * n):
	if i % 2 == 0:
		if ab[i][1] == 0:
			ans += ab[i][0]
	else:
		if ab[i][1] == 1:
			ans -= ab[i][0]

print(ans)
