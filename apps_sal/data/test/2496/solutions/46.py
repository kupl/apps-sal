import math
import functools


def primes(n):
    is_prime = [1] * (n + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    D_prime = [i for i in range(n + 1)]
    D_prime[0] = 0
    D_prime[1] = 1
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            D_prime[i] = i
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = 0
            D_prime[j] = i
    return D_prime


Fnum_list2 = []
N = int(input())
A = list(map(int, input().split()))


A.sort()
Amax = A[-1]
Fnum_list2 = primes(Amax)
j = A[0]
ans = 1
Ai_primes = set()
Ai_primes_add = []
gcd_num = 0
for i in range(len(A)):
    p = A[i]
    while p != 1:
        j = p
        p = int(p / Fnum_list2[j])
        if Fnum_list2[j] in Ai_primes:
            ans = 0
        else:
            Ai_primes_add.append(Fnum_list2[j])
    if Fnum_list2[j] in Ai_primes:
        break
    else:
        Ai_primes |= set(Ai_primes_add)
        Ai_primes_add.clear()

gcd_num = functools.reduce(math.gcd, A)

if ans == 0:
    if gcd_num == 1:
        ans = 2

if ans == 1:
    print("pairwise coprime")
else:
    if ans == 2:
        print("setwise coprime")
    else:
        print("not coprime")
