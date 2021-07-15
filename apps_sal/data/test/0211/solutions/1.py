n, m, k = map(int, input().split())
mod = 1000000000 + 9
x = m - (n // k * (k-1) + (n%k))
if (x <= 0):
	print (m % mod)
else:
	print(((m-x) + ((pow(2, x + 1, mod) + 2 * mod)-2)*k - x*(k-1))%mod)
