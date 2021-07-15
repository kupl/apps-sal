import random

n = int(input())
a = list(map(int, input().split()))

limit = min(8, n)
iterations = [x for x in range(n)]
random.shuffle(iterations)
iterations = iterations[:limit]

def factorization(x):
	primes = []
	i = 2
	while i * i <= x:
		if x % i == 0:
			primes.append(i)
			while x % i == 0: x //= i
		i = i + 1
	if x > 1: primes.append(x)
	return primes

def solve_with_fixed_gcd(arr, gcd):
	result = 0
	for x in arr:
		if x < gcd: result += (gcd - x)
		else:
			remainder = x % gcd
			result += min(remainder, gcd - remainder)
	return result

answer = float("inf")
prime_list = set()
for index in iterations:
	for x in range(-1, 2):
		tmp = factorization(a[index]-x)
		for z in tmp: prime_list.add(z)

for prime in prime_list:
	answer = min(answer, solve_with_fixed_gcd(a, prime))
	if answer == 0: break

print(answer)
