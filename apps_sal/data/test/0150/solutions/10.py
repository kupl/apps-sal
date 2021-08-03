from math import sqrt
limit = 2 * 1000000000
primes = [True for i in range(int(sqrt(limit)) + 1)]
tes = int(sqrt(sqrt(limit))) + 1
for i in range(2, tes):
    if primes[i]:
        for z in range(i * i, int(sqrt(2 * 1000000000)) + 1, i):
            primes[z] = False


def ptest(n):
    nonlocal primes
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i]:
            if n % i == 0:
                return 0
    return 1


i = int(input().strip())
if i % 2 == 0:
    if i == 2:
        print(1)
    else:
        print(2)
else:
    if ptest(i):
        print(1)
    elif ptest(i - 2):
        print(2)
    else:
        print(3)
