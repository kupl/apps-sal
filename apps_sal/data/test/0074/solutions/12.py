import math
n = int(input())
primes = [2]
for i in range(3, math.ceil(n ** 0.5) + 1):
    for p in primes:
        if i % p == 0:
            break
    else:
        primes.append(i)


def isprime(x):  # x < n
    if x == 1:
        return False
    for p in primes:
        if x % p == 0 and x > p:
            return False
    else:
        return True


if isprime(n):
    print(1)
    print(n)
else:
    x1 = n
    while not isprime(x1):
        x1 -= 2
    if isprime(n - x1):
        print(2)
        print(x1, n - x1)
    else:
        l = n - x1
        for x2 in primes:
            if isprime(l - x2):
                print(3)
                print(x1, x2, l - x2)
                break
        else:
            print('nu chto podelat...')
