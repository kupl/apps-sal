N = int(input())
A = list(map(int, input().split()))
number_to_prime = [0] * (10 ** 6 + 1)
for i in range(2, 10 ** 6 + 1):
    if not number_to_prime[i]:
        j = 1
        while j * i <= 10 ** 6:
            number_to_prime[j * i] = i
            j += 1


def is_pair_copr(A):
    import numpy as np
    U = 1 << 20
    div_p = np.arange(U)
    for p in range(2, U):
        if div_p[p] != p:
            continue
        div_p[p::p] = p
    used = np.zeros(U, np.bool_)
    for x in A:
        while x > 1:
            p = div_p[x]
            while x % p == 0:
                x //= p
            if used[p]:
                return False
            used[p] = True
    return True


def is_pairwise():
    used_primes = set()
    pairwise_flag = 1
    for a in A:
        curr_primes = set()
        while a > 1:
            prime = number_to_prime[a]
            curr_primes.add(prime)
            a //= prime
        if used_primes & curr_primes:
            pairwise_flag = 0
            break
        else:
            used_primes = used_primes | curr_primes
    return pairwise_flag


def is_setwise(*A):
    import math
    from functools import reduce
    return reduce(math.gcd, A) == 1


if is_pair_copr(A):
    print('pairwise coprime')
elif is_setwise(*A):
    print('setwise coprime')
else:
    print('not coprime')
