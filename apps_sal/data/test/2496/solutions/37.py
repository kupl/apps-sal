N = int(input())
A = list(map(int, input().split()))
number_to_prime = [0] * (10 ** 6 + 1)
for i in range(2, 10 ** 6 + 1):
    if not number_to_prime[i]:
        j = 1
        while j * i <= 10 ** 6:
            number_to_prime[j * i] = i
            j += 1


def is_pairwise():
    used_primes = [False] * (10 ** 6 + 1)
    pairwise_flag = 1
    for a in A:
        curr_primes = set()
        while a > 1:
            prime = number_to_prime[a]
            while a % prime == 0:
                a //= prime
            if used_primes[prime]:
                return False
            used_primes[prime] = 1
    return True


def is_setwise(*A):
    import math
    from functools import reduce
    return reduce(math.gcd, A) == 1


if is_pairwise():
    print('pairwise coprime')
elif is_setwise(*A):
    print('setwise coprime')
else:
    print('not coprime')
