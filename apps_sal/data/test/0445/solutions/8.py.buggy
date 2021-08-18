import sys


def get_primes(n: int):
    from itertools import chain
    from array import array
    primes = {2, 3}
    is_prime = (array('b', (0, 0, 1, 1, 0, 1, 0))
                + array('b', (1, 0, 0, 0, 1,0 ))*((n-1)//6))

    for i in chain.from_iterable((list(range(5, n + 1, 6)), list(range(7, n + 1, 6)))):
        if is_prime[i]:
            primes.add(i)
            for j in range(i * 3, n + 1, i * 2):
                is_prime[j] = 0

    return is_prime, primes


n = int(input())
a = list(map(int, input().split()))
is_prime, primes = get_primes(2 * 10**6)

one_count = a.count(1)
if one_count > 1:
    for i in range(n):
        if a[i] != 1 and is_prime[a[i] + 1]:
            print(one_count + 1)
            print(*([1] * one_count + [a[i]]))
            return
    else:
        print(one_count)
        print(*([1] * one_count))
else:
    for i in range(n):
        for j in range(n):
            if i != j and is_prime[a[i] + a[j]]:
                print(2)
                print(a[i], a[j])
                return
    else:
        print(1)
        print(a[0])
