def solve(n, k, d, e, memo):
	if n < 0:
		return 0
	if n == 0:
		return e
	if (n, e) in memo:
		return memo[(n, e)]
	ans = 0
	for i in range(1, d):
		ans += solve(n - i, k, d, e, memo)
	for i in range(d, k + 1):
		ans += solve(n - i, k, d, 1, memo)
	memo[(n, e)] = ans % 1000000007
	return ans % 1000000007

n, k, d = (int(x) for x in input().split())
print(solve(n, k, d, 0, dict()))

