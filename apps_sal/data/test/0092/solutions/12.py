mod = (1 << 30)
memo = dict()

def dp(x):
	if x in memo:
		return memo[x]
	res, q, t = 1, 2, x
	while q * q <= x:
		r = 1
		while x % q == 0:
			x /= q
			r += 1
		res = (res * r) % mod
		q += 1
	if x > 1:
		res = (res * 2) % mod
	memo[t] = res
	return res

a, b, c = sorted(map(int, input().split()))
res = 0
for i in range(1, a+1):
	for j in range(1, b+1):
		for k in range(1, c+1):
			res = (res + dp(i * j * k)) % mod
print(res)

