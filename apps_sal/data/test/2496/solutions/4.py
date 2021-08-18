from functools import reduce
from bisect import bisect_left
import sys
import math


def osa_k(a):
    tmp = set()
    while a > 1:
        tmp.add(sieve[a])
        a //= sieve[a]
    return tmp


input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
used = set()

gcd_a = reduce(math.gcd, A)
if gcd_a != 1:
    ans = "not coprime"

else:
    MAXN = 10**6 + 10
    sieve = [i for i in range(MAXN + 1)]
    p = 2
    while p * p <= MAXN:
        if sieve[p] == p:
            for q in range(2 * p, MAXN + 1, p):
                if sieve[q] == q:
                    sieve[q] = p
        p += 1

    ans = "pairwise coprime"
    for a in A:
        aa = osa_k(a)
        if used & aa:
            ans = "setwise coprime"
            break
        used |= aa

print(ans)
