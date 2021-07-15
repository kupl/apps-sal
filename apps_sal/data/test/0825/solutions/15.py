N = int(input())

def Prime_Factorize(n):
    primes = []
    while n%2 == 0:
        n//=2
        primes.append(2)
    f = 3
    while f*f <= n:
        if n%f == 0:
            n//=f
            primes.append(f)
        else:
            f += 2
    if n != 1:
        primes.append(n)
    return primes

Primes = Prime_Factorize(N)
cnt = 0
for p in Primes:
    e = 1
    z = p
    while (N%z == 0) and (N >= z):
        N //= z
        e += 1 
        z = p**e
        cnt += 1
    while N%p == 0:
        N //= p
print(cnt)
