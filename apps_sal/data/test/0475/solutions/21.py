'''input
3 2 1
6 3 2
5 3 0
3 3 1
3 3 0
'''
n, m, k = list(map(int, input().split()))
MOD  = 998244353
ans = m * pow(m - 1, k, MOD) % MOD
'''
for i in range(k + 1):
	if i & 1:
		ans -= m * pow(m - 1, k - i, MOD)
	else:
		ans += m * pow(m - 1, k - i, MOD)
'''


for i in range(n - k, n):
	ans = ans * i
for i in range(n - k, n):
	# print(n - 1 - i)
	ans = ans // (n - i)
'''
for i in range(1, k + 1):
	print(ans)
	ans = ans * (n - 1 - i) * pow(i, MOD - 2, MOD) % MOD
'''
print(ans % MOD)

