a, b, n, x = map(int, input().split())
MOD = 10 ** 9 + 7
ans = pow(a, n, MOD) * x
if a > 1:
	tmp = (pow(a, n, MOD) - 1)
	if tmp < 0:
		tmp += MOD
	tmp *= pow(a - 1, MOD - 2, MOD)
	tmp *= b
else:
	tmp = n * b
print((ans + tmp) % MOD)
