memo = [[None for i in range(50)] for j in range(50)]
def opt(n,k): # exponents must be >= k
	if n < k:
		return 0
	else:
		if memo[n][k]==None:
			memo[n][k] = max(1+opt(n-k,k+1),opt(n,k+1))
		return memo[n][k]

def prime_factorize(n):
	pf = {}
	d = 2
	orig_n = n
	while d*d <= orig_n:
		while n%d==0:
			pf[d] = pf.get(d,0)+1
			n //= d
		d += 1

	if n > 1:
		pf[n] = 1
	return pf 

print(sum([opt(e,1) for e in prime_factorize(int(input())).values()]))
