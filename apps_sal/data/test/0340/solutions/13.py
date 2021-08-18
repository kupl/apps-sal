from collections import Counter
import math


def primeFactors(n):

    while n % 2 == 0:
        yield 2
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            yield i
            n = n / i

    if n > 2:
        yield n


def get_prime_factorization(n):
    if(n == 1):
        return {1: 1}
    primes = {}
    for prime in primeFactors(n):
        prime = int(prime)
        if(prime in primes):
            primes[prime] += 1
        else:
            primes[prime] = 1
    return primes


def next_power_of_2(n):
    return int(math.pow(2, math.ceil(math.log(n) / math.log(2))))


def solution(n):

    pf = get_prime_factorization(n)

    lp = 0
    for key, val in list(pf.items()):
        lp = max(lp, val)

    np2 = next_power_of_2(lp)
    ans = 1
    for key, val in list(pf.items()):
        ans *= key

    moves = 0
    for key, val in list(pf.items()):
        if(val != np2):
            moves = 1
            break
    moves += int(math.log2(np2))

    print(ans, moves)


def __starting_point():

    n = [int(val) for val in input().split()][0]

    solution(n)


__starting_point()
