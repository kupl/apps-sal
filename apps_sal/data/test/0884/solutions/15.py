import math

mod = 998244353

factmod = [0]*5001

factmod[0] = 1
for i in range(1, 5001):
	factmod[i] = (factmod[i-1] * i) % mod

	
def nCk(n,k):
	'''if k > n//2:
		k=n-k
	ret = 1
	for i in range(1, k+1):
		ret = ret * (n-i+1) // i
	return ret	'''
	if n==a:
		return aCks[k]
	if n==b:
		return bCks[k]
	if n==c:
		return cCks[k]
	xxx
	
	#return math.factorial(n) // math.factorial(k) // math.factorial(n-k)

def calc(x,y):
	nonlocal mod
	x,y = min(x,y), max(x,y)
	sm = 0
	for i in range(x+1):
		
		sm += ((nCk(x, i)) % mod) * ((nCk(y, i)) % mod) * ((factmod[i]) % mod)
		sm = sm % mod
	return sm

#print(factmod[5], nCk(5, 3))

a,b,c = list(map(int, input().split()))

aCks = [1]*(a+1)
for i in range(1, a):
	aCks[i] = aCks[i-1] * (a-i+1) // (i)
aCks = [aCks[i] % mod for i in range(len(aCks))]
#print(aCks[:a+1])

bCks = [1]*(b+1)
for i in range(1, b):
	bCks[i] = bCks[i-1] * (b-i+1) // (i)
bCks = [bCks[i] % mod for i in range(len(bCks))]

cCks = [1]*(c+1)
for i in range(1, c):
	cCks[i] = cCks[i-1] * (c-i+1) // (i)
cCks = [cCks[i] % mod for i in range(len(cCks))]

#print(aCks)
#print(bCks)
#print(cCks)
	

print((calc(a,b)*calc(b,c)*calc(a,c)) % mod)


