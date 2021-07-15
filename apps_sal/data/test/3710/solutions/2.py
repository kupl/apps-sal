def sieze_prime(n):
    sieze = [True]*(n+1)
    sieze[0] = sieze[1] = False
    i = 2
    while i * i <= n:
        if sieze[i]:
            for j in range(2*i, n+1, i):
                sieze[j] = False
            # end for
        # end if
        i = i + 1
    # end while
    primes = range(0, n+1)
    primes = filter(lambda x : sieze[x], primes)
    return primes
# end def

def factorize(n):
    nonlocal primes
    factors = []
    i = 0;
    while primes[i]**2 <= n:
        p = primes[i]
        if n % p == 0:
            factor = [primes[i], 1]
            n //= p
            while n % p == 0:
                n //= p
                factor[1] += 1
            # end while
            factors.append(factor)
        # end if
        i += 1
    # end while
    if not n==1: factors.append([n, 1])
    return factors
# end def

primes = None

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    nonlocal primes
    primes = list(sieze_prime(1000000))
    n, k = map(lambda x : int(x), input().split())
    c = set(map(lambda x : int(x), input().split()))
    factors = factorize(k)
    success = True
    for prime, power in factors:
        factor = prime**power
        if any(map(lambda x : int(x) % factor==0, c)):
            continue
        else:
            success = False
            break
    if success: print("Yes")
    else: print("No")

main()
