import copy
import random
import bisect
import fractions
import math
import sys
import collections
from decimal import Decimal
mod = 10 ** 9 + 7
sys.setrecursionlimit(mod)
d = collections.deque()


def LI():
    return list(map(int, sys.stdin.readline().split()))


(N, M) = LI()


def primes(n):
    cnt = collections.defaultdict(int)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                cnt[i] += 1
                n //= i
    if n != 1:
        cnt[n] += 1
    return cnt


'\nO(N ** 0.5)で計算できる約数列挙\n\nN = 20\nmake_divisors(20) = [1,2,4,5,10,20]\n'


def make_divisors(n):
    (lower_divisors, upper_divisors) = ([], [])
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


divs = make_divisors(M)
ans = -1
for (i, divisior) in enumerate(divs):
    if divisior > M // N:
        break
    else:
        ans = divisior
print(ans)
