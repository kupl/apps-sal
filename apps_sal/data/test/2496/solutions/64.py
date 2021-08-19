from math import gcd
from functools import reduce
N = int(input())
A = list(map(int, input().split()))


def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


l = primes(max(A))
# print(l)
d = [0] * max(A)
for i in A:
    d[i - 1] = 1
# print(d)
# for i in l:
#  print(d[i-1::i])
if reduce(gcd, A) > 1:
    print('not coprime')
elif all(sum(d[i - 1::i]) <= 1 for i in l):
    print('pairwise coprime')
else:
    print('setwise coprime')
