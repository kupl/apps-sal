import math, re, itertools as it;prime = lambda n: len([i for i in range(2, int(math.sqrt(n) + 1)) if n % i == 0]) == 0;gcd = lambda a, b: gcd(b, a % b) if b else a;fact = lambda x: x * fact(x - 1) if x else 1;bino = lambda n, k: fact(n) / fact(k) / fact(n - k);fib11 = lambda n: 1 if n < 2 else fib11(n - 1) + fib11(n - 2);fib01 = lambda n: 0 if n == 0 else 1 if n == 1 else fib01(n - 1) + fib01(n - 2);sumofd = lambda x: x if x < 10 else sumofd(x // 10) + x % 10

n, l = map(int, input().split(' '))
k = list(map(int, input().split()))
s = list(map(int, input().split()))
f = False
for i in range(l):
	for j in range(len(k)):
		k[j] -= 1
		
		if k[j] < 0:
			k[j] = l - 1
	k.sort()
	if k == s:
		f = True
print('YES' if f else 'NO')
