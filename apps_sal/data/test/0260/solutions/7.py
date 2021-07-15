MX_BIT = 64
C = [[int(0) for i in range(MX_BIT)] for j in range(MX_BIT)]

def ck(x, i):
	return (x>>i) & 1
def tot_bits(x):
	x = bin(x)[2:]
	return len(x)
def mkt():
	C[0][0] = 1
	for i in range (1, MX_BIT):
		for j in range (i+1):
			C[i][j] = C[i-1][j] + (C[i-1][j-1] if j else 0)
def solve(x, k):
	a = 0
	for i in reversed(list(range(MX_BIT))):
		if ck(x, i) != 0:
			a += C[i][k]
			k -= 1
		if k == 0:
			break
	return a
mkt()
m, k = list(input().split())
m = int(m)
k = int(k)
l = 1
r = 1e18
if not m:
    l = 1
else:
    while l < r:
    	mid = int((l + r) // 2)
    	if (solve(2*mid, k) - solve(mid, k)) < m :
    		l = mid + 1
    	else:
    		r = mid
print(l)

