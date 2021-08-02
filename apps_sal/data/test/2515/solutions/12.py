from itertools import accumulate
n = int(input())


def gen_primes(limit):
    prime_table = [True] * (limit + 1)
    prime_table[0] = False
    prime_table[1] = False
    for i in range(2, int(limit**.5) + 1):
        prime_table[i + i::i] = [False] * (limit // i - 1)
    return prime_table


primes = gen_primes(10**5)
like2017 = [0] * len(primes)

for i in range(1, len(primes), 2):
    if primes[i] and primes[(i + 1) // 2]:
        like2017[i] = 1

like2017 = list(accumulate(like2017))
for _ in range(n):
    l, r = list(map(int, input().split()))
    print(like2017[r] - like2017[l - 1])
