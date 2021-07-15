from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

n = int(max(a)**.5)
mark = [True]*(n+1)
primes = []
for i in range(2,n+1):
	if mark[i]:
		primes.append(i)
		for j in range(i, n+1, i): mark[j] = False
del mark
d = defaultdict(int)
ans = 0

for i in a:
	t, t1 = (), ()
	for j in primes:
		if i == 1:break
		elif i%j == 0:
			x = 0
			while i%j==0: 
				i//=j
				x += 1
			z = x%k
			if z:
				t += (j,z)
				t1 += (j,k-z)
	if i != 1:
		t += (i,1)
		t1 += (i,k-1)

	ans += d[t1]
	d[t] += 1
print(ans)
