n = int(input())
primes = {}
for i in range(2, n):
	while n%i == 0:
		n /= i 
		if i in primes:
			primes[i] += 1
		else:
			primes[i] = 1
if len(primes) == 0:
	print(n, 0)
	return
from math import ceil, log2
pow2 = pow(2, ceil(log2(max(primes.values()))))
flag = 0
for i in primes:
	if primes[i] != pow2:
		flag = 1
		break
ans = 1
for i in primes:
	ans*=i
print(ans, int(log2(pow2)) + flag)
