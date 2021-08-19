# -*- coding: utf-8 -*-
import sys
from collections import deque
from collections import defaultdict
from itertools import accumulate

import heapq
import collections
import itertools
import bisect
import copy
import math
sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def zz(): return list(map(int, sys.stdin.readline().split()))


def z(): return int(sys.stdin.readline())


def S(): return sys.stdin.readline()[:-1]


def C(line): return [sys.stdin.readline() for _ in range(line)]


def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


max_ = pow(10, 5) + 2
primes = get_sieve_of_eratosthenes(max_)
num_lile2017 = [0] * max_
primes2 = []
for prime in primes:
    primes2.append(2 * prime - 1)
like2017 = sorted(list(set(primes2) & set(primes)))
for i in range(3, max_, 2):
    if (i in like2017):
        num_lile2017[i] = 1
num_lile2017 = list(accumulate(num_lile2017))
# print(num_lile2017)

Q = z()
for i in range(Q):
    l, r = zz()
    print((num_lile2017[r] - num_lile2017[l - 1]))
