MOD = 998244353
n, m, l, r = map(int, input().split())
k = r-l
if (n*m) % 2 == 1:
	print(pow(k+1, n*m, MOD))
elif k%2 == 1:
	print((pow(k+1, n*m, MOD) * 499122177) % MOD)
else:
	print(((pow(k+1, n*m, MOD) + 1) * 499122177) % MOD)
