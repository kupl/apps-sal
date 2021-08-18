

import sys
sys.setrecursionlimit(10**5 + 1)

inf = int(10 ** 20)
max_val = inf
min_val = -inf


def RW(): return sys.stdin.readline().strip()
def RI(): return int(RW())
def RMI(): return [int(x) for x in sys.stdin.readline().strip().split()]
def RWI(): return [x for x in sys.stdin.readline().strip().split()]


LIMIT = 2750132
primes = [0] * LIMIT
pindex = [0] * LIMIT

index = 1
for i in range(2, LIMIT):
    if primes[i] == 0:
        pindex[i] = index
        index += 1
        for j in range(i * i, LIMIT, i):
            if primes[j] == 0:
                primes[j] = i

lens = RI()
arrs = sorted(RMI())[::-1]
d = dict()
for x in arrs:
    if d.get(x, 0) == 0:
        if primes[x] == 0:
            print(pindex[x], end=" ")
            d[pindex[x]] = d.get(pindex[x], 0) + 1
        else:
            print(x, end=" ")
            d[x // primes[x]] = d.get(x // primes[x], 0) + 1
    else:
        d[x] = d.get(x, 0) - 1
