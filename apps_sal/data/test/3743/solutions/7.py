from math import sqrt, floor

def sieve(n):
	primes = [True] * (n + 1)
	primes[0] = False
	primes[1] = False
	for i in range(2, n + 1):
		if i*i > n:
			break

		# if primes[i] == True:
		if primes[i] == False:
			continue

		# for j in range(2*i, n + 1):
		for j in range(2*i, n + 1, i):
			# if j == 5:
			# 	print('i: ', i)
			primes[j] = False

	return primes


def run_testcase():
	number = int(input())

	# print(sieve(number))
	# print(zip(range(number), sieve(number)))
	# print(list(zip(range(number), sieve(number))))
	# print(list(zip(range(number + 1), sieve(number))))

	# prime_divisors_count = 0

	# # while number % 2 == 0:
	# # 	prime_divisors_count += 1

	# last_prime_divisor = 2


	# # def sieve():


	# if number % last_prime_divisor == 0:
	# 	prime_divisors_count += 1
	# 	while number % last_prime_divisor == 0:
	# 		# number /= last_prime_divisor
	# 		number = number // last_prime_divisor

	# num_sqrt = sqrt(number)

	# # primes = [True] * (int(sqrt) + 1)
	# # primes = [True] * int(sqrt)
	# # primes = [True] * (int(sqrt) + 1)
	# # primes = [True] * (floor(num_sqrt) + 1)
	# primes = [True] * (floor(num_sqrt) + 2)
	# primes[0] = False
	# primes[1] = False

	# # print(len(primes))

	# # for i in range(len(primes)):
	# # for i in range(len(2, primes)):
	# for i in range(2, len(primes)):
	# 	# for j in range(i)
	# 	if i*i >= num_sqrt:
	# 		break

	# 	# if prime[i] == True:
	# 	if primes[i] == True:
	# 		continue

	# 	# j = 0
	# 	j = 2 * i
	# 	while j < len(primes):
	# 		# print(j)
	# 		primes[j] = False
	# 		j += i

		# print('test')

	num_sqrt = sqrt(number)

	# primes = sieve(num_sqrt)
	primes = sieve(floor(num_sqrt))

	prime_divisors_count = 0
	last_prime_divisor = 0

	for value, prime in enumerate(primes):
		if prime:
			if number % value == 0:
				last_prime_divisor = value
				prime_divisors_count += 1
				if prime_divisors_count >= 2:
					return 1
				while number % value == 0:
					number = number // value
				if number == 1:
					return value
				else:
					return 1



	# for value, prime in primes:
	for value, prime in enumerate(primes):
		if prime:
			# print(value)
			if number % value == 0:
				last_prime_divisor = value
				prime_divisors_count += 1
				if prime_divisors_count >= 2:
					return 1


	# return last_prime_divisor
	# return last_prime_divisor if last_prime_divisor != 0 else number

	# print(last_prime_divisor)

	# if number == 2:
	# 	return 2

	# if last_prime_divisor ** 2 == number:
		# return last_prime_divisor
	if last_prime_divisor == 0:
		return number
	elif last_prime_divisor ** 2 == number:
		return last_prime_divisor
	else:
		return 1

	return last_prime_divisor if last_prime_divisor != 0 else number

# testcase_count = int(input())

# for i in range(testcase_count):
# 	print(str(run_testcase()))
	# run_testcase()
# run_testcase()
print(str(run_testcase()))

