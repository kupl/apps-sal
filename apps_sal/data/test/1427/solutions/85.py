import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def prime_factorization(n):
    res = []
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            res.append([i, ex])
    if n != 1:
        res.append([n, 1])
    return res


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    prime = [0] * max(A)
    for a in A:
        primes = prime_factorization(a)
        for (num, ex) in primes:
            prime[num - 1] = max(prime[num - 1], ex)
    L = 1
    for i in range(len(prime)):
        if prime[i] == 0:
            continue
        L *= pow(i + 1, prime[i])
    res = 0
    for a in A:
        res += L * pow(a, mod - 2, mod)
        res %= mod
    print(res)


def __starting_point():
    resolve()


__starting_point()
