import math

x, n = map(int, input().split())

maxPrime = int(math.sqrt(x) + 1)

isPrime = [True] * maxPrime

primes = []

for i in range(2, maxPrime):
    if(x % i == 0):
        primes.append(i)

    while (x % i) == 0:
        x = x // i

if(x > 1):
    primes.append(x)

sol = 1


def quickPow(x, power):
    if(power == 1):
        return x

    ans = quickPow(x, power // 2)

    ans *= ans

    if(power % 2) == 1:
        ans *= x

    return ans % 1000000007


for prime in primes:
    i = prime

    while(i <= n):
        sol = (sol * quickPow(prime % 1000000007, (n // i))) % 1000000007
        i *= prime

print(sol)
