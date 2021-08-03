import math
from bisect import bisect_left


def sieve(n):
    isPrimeList = [True] * (n + 1)
    isPrimeList[0] = False
    isPrimeList[1] = False

    for i in range(2, int(math.sqrt(n))):
        if isPrimeList[i]:
            for j in range(i * 2, n, i):
                isPrimeList[j] = False

    return isPrimeList


primes = sieve(3 * 10**6)
p = []
for i in range(3 * 10**6 + 1):
    if primes[i]:
        p.append(i)

n = int(input())
b = list(map(int, input().split()))
trihard = [0] * 3000001
for i in b:
    trihard[i] = trihard[i] + 1
moveCount = 0
a = []
for i in range(3000000, -1, -1):
    while trihard[i]:
        if primes[i]:
            pos = bisect_left(p, i)
            a.append(str(pos + 1))
            trihard[i] -= 1
            trihard[pos + 1] -= 1
        else:
            for j in p:
                if i % j == 0:
                    a.append(str(i))
                    trihard[i] -= 1
                    trihard[i // j] -= 1
                    break
print(" ".join(a))
