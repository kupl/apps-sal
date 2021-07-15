n, m, k = map(int, input().split())

if n + m - 2 < k:
	print(-1)
	return

def divisors(n):
	div = set()

	for i in range(1, int(n ** (1 / 2)) + 1):
		if n % i == 0:
			div.add(i)
			div.add(n // i)

	return [*div]

def solve(n, m, k):
	div = divisors(n)
	ans = 0

	for i in div:
		if i - 1 > k: continue
		ans = max(ans, (n // i) * (m // (k - i + 2)))

	return ans

print(max(solve(n, m, k), solve(m, n, k)))
