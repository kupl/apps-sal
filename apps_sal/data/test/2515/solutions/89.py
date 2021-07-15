import bisect
 
N = 10 ** 5
primes = [True] * (N + 1)
primes[0] = primes[1] = False
for i in range(2, int(len(primes) ** 0.5 + 1)):
    for j in range(i + i, len(primes), i):
        primes[j] = False
primes = [i for i in range(len(primes)) if primes[i]]
targets = [x for x in primes if (x + 1) // 2 in primes]
 
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    x = bisect.bisect_left(targets, l)
    y = bisect.bisect_right(targets, r)
    print(y - x)
