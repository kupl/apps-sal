def fac(n):
	if n == 0:
		return 1
	ans =  1
	for i in range(2, n + 1):
		ans *= i
	return ans


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
ans = fac(n - m)
ans //= fac(a[0] - 1)
for i in range(1, m):
	ans //= fac(a[i] - a[i - 1] - 1)
	if a[i] - a[i - 1] - 1 != 0:
		ans *= 2 ** (a[i] - a[i - 1] - 2)
ans //= fac(n - a[m - 1])
print(ans % 1000000007)


