import math
from sys import stdin
	
def factorize(x):
	i = 2
	y = x
	prime_factors = []
	while i * i <= x:
		if y % i == 0:
			prime_factors.append(i)
			while y % i == 0:
				y //= i
		i += 1
	if y > 1:
		prime_factors.append(y)
	return prime_factors

def main():
	n = int(input())
	prime_factors = factorize(n)
	
	if n == 1 or len(prime_factors) > 1:
		print(1)
	elif n > prime_factors[0]:
		print(prime_factors[0])
	else:
		print(n)

def __starting_point():
	main()
__starting_point()
