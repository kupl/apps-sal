n, m, k = map(int, input().split())
a = list(map(int, input().split()))
mn = 10 ** 9
for i in range(n):
	if i != m - 1 and a[i] <= k and a[i] != 0:
		mn = min(mn, abs(m - i - 1) * 10)
print(mn)
