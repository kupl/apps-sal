from itertools import accumulate


def sieve(n):
    from math import sqrt
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False
    for i in range(int(sqrt(n)) + 1):
        if is_prime[i]:
            for k in range(2, n // i + 1):
                is_prime[i * k] = False
    return is_prime


def is_like2017(n):
    for i in range(n + 1):
        if is_primeL[i]:
            #print(i, (i+1)//2)
            if is_primeL[(i + 1) // 2]:
                is_likeL[i] = True


n = 100000
is_primeL = sieve(n)
is_likeL = [False for _ in range(n + 1)]
is_like2017(n)


cumL = list(accumulate(is_likeL))
cumL[0] = 0

q = int(input())
for _ in range(q):
    l, r = list(map(int, input().split()))
    print((cumL[r] - cumL[l - 1]))
