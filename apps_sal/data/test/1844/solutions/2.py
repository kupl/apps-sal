from sys import *

maxn = 3 * 10 ** 5 + 5
fre = [0] * maxn
divi = [0] * maxn
isprime = [0] * maxn
prime = []


def seive(n):
    for i in range(n):
        isprime[i] = True
    for i in range(2, n):
        if isprime[i] is True:
            prime.append(i)
        for j in range(1, n):
            if i * j >= n:
                break
            isprime[i * j] = False
            divi[i] += fre[i * j]


mobius = [0] * maxn


def calc_mobius(n):
    for i in range(1, n):
        mobius[i] = 1
    for p in prime:
        if p * p >= n:
            break
        x = p * p
        for j in range(x, n, x):
            mobius[j] = 0
    for p in prime:
        for j in range(p, n, p):
            mobius[j] *= -1


fact = [1] * 10


def calc_fact():
    fact[0] = 1
    for i in range(1, 10):
        fact[i] = i * fact[i - 1]


def nCr(n, r):
    if n < r:
        return 0
    if n is r:
        return 1
    pro = 1
    for i in range(r):
        pro *= (n - i)
    pro //= fact[r]
    return pro


def count_coprime(r):
    coprime = 0
    for d in range(1, maxn):
        ncr = nCr(divi[d], r)
        coprime += mobius[d] * ncr
    return coprime


def __starting_point():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    for i in arr:
        if i is 1:
            print(1)
            return
        fre[i] += 1
    divi[1] = n
    seive(maxn)
    calc_mobius(maxn)
    calc_fact()
    for r in range(2, 8):
        coprime = count_coprime(r)
        if coprime > 0:
            print(r)
            return
    print(-1)


__starting_point()
