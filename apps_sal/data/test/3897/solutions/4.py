MOD = 10 ** 9 + 7


def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    l = []
    for p in range(2, n):
        if prime[p]:
            l.append(p)
    return l


def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = num * (n - i) % p
        den = den * (i + 1) % p
    return num * pow(den, p - 2, p) % p


primes = SieveOfEratosthenes(31623)
n = int(input())
l = [int(zax) for zax in input().split()]
map = {}
for x in l:
    for p in primes:
        if p > x:
            break
        if x % p == 0:
            check = False
            while x % p == 0:
                if p in map:
                    map[p] += 1
                else:
                    map[p] = 1
                x //= p
    if x != 1:
        if x in map:
            map[x] += 1
        else:
            map[x] = 1
count = 1
for x in map:
    count *= ncr(n - 1 + map[x], n - 1, MOD)
    count %= MOD
count %= MOD
print(count)
