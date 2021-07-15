from sys import stdin, stdout
 
ii = lambda: int(stdin.readline())
mi = lambda: list(map(int, stdin.readline().strip().split()))
li = lambda: list(mi())

MOD = int(1000000007)

def binpow(a, b, m):
	a %= m
	res = 1
	while (b > 0):
		if (b & 1):
			res = res * a % m
		a = a * a % m
		b >>= 1
	return res

x, n = mi()
fac = []
tmp = int(x)
if (tmp % 2 == 0):
	fac.append(2)
	while(tmp % 2 == 0):
		tmp = tmp // 2
i = 3
while (i * i <= tmp):
	if (tmp % i == 0):
		fac.append(i)
		while(tmp % i == 0):
			tmp = tmp // i
	i += 2

if (tmp > 2):
	fac.append(tmp)
ans = 1
for p in fac:
	prod = p
	i = 1
	fin = 0
	while (prod <= n):
		times = (n // prod) - (n // (prod * p))
		fin += (i * times)
		prod *= p
		i += 1
	ans = (ans * binpow(p, fin, MOD)) % MOD
print(ans)

