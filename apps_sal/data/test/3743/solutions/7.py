from math import sqrt, floor


def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, n + 1):
        if i * i > n:
            break
        if primes[i] == False:
            continue
        for j in range(2 * i, n + 1, i):
            primes[j] = False
    return primes


def run_testcase():
    number = int(input())
    num_sqrt = sqrt(number)
    primes = sieve(floor(num_sqrt))
    prime_divisors_count = 0
    last_prime_divisor = 0
    for (value, prime) in enumerate(primes):
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
    for (value, prime) in enumerate(primes):
        if prime:
            if number % value == 0:
                last_prime_divisor = value
                prime_divisors_count += 1
                if prime_divisors_count >= 2:
                    return 1
    if last_prime_divisor == 0:
        return number
    elif last_prime_divisor ** 2 == number:
        return last_prime_divisor
    else:
        return 1
    return last_prime_divisor if last_prime_divisor != 0 else number


print(str(run_testcase()))
