import math
n, k = list(map(int, input().split()))
a, b = list(map(int, input().split()))

nk = n * k
mi = 1e12
ma = 0

def solve(st):
	nonlocal mi, ma
	for i in range(n):
		en = i * k + 1 + b
		if en < st:
			en += nk
		res = nk // math.gcd(en - st, nk)
		mi = min(mi, res)
		ma = max(ma, res)
		
		en = (i + 1) * k + 1 - b
		if en < st:
			en += nk
		res = nk // math.gcd(en - st, nk)
		mi = min(mi, res)
		ma = max(ma, res)

solve(1 + a)
solve(k + 1 - a)

print(mi, ma)

