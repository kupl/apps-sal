n, m, k = map(int, input().split())
ans = 1
for i in range(k):
	ans *= (n - 1 - i)
	ans //= (i + 1)
print((ans * m * (m - 1) ** k) % 998244353)
