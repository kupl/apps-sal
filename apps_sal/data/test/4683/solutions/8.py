import math
prime = [True for i in range(10**6+1)]
def SieveOfEratosthenes(n): 
	p = 2
	while (p * p <= n): 
		if (prime[p] == True):
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1

def __starting_point():
	N = int(input())
	L = list(map(int,input().split()))
	MOD =  10**9 + 7
	sum_L = sum(L)
	ans = 0
	for i in range(N - 1):
		sum_L = sum_L - L[i]
		ans = (ans + sum_L*L[i])%MOD
	print(ans)





__starting_point()
