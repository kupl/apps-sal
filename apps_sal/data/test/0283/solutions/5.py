
def primesSieve(limit):
    def internalPrimesSieve(limit):
        a = [True] * limit # Initialize the primality list
        a[0] = a[1] = False

        for (i, isprime) in enumerate(a):
            if isprime:
                yield i
                for n in range(i*i, limit, i): # Mark factors non-prime
                    a[n] = False
    return [p for p in internalPrimesSieve(limit)]

n = int(input())
primes = primesSieve(1000002)
for i in range(1,1001):
    if n*i + 1 not in primes:
        print(i)
        break

