import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(pow(n, 0.5)) + 1):
        if n % k == 0:
            return False
    return True


def resolve():
    n = int(input())
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)

    fact = []
    for prime in primes:
        ex = 0
        p = prime
        while n // p:
            ex += n // p
            p *= prime
        fact.append(ex)

    cnt_74 = cnt_24 = cnt_14 = cnt_4 = cnt_2 = 0
    for i in fact:
        if i >= 74:
            cnt_74 += 1
        if i >= 24:
            cnt_24 += 1
        if i >= 14:
            cnt_14 += 1
        if i >= 4:
            cnt_4 += 1
        if i >= 2:
            cnt_2 += 1

    res1 = max(0, cnt_24 * (cnt_2 - 1))
    res2 = (cnt_4 * (cnt_4 - 1)) // 2 * max(0, cnt_2 - 2)
    res3 = max(0, cnt_14 * (cnt_4 - 1))
    print((cnt_74 + res1 + res2 + res3))


def __starting_point():
    resolve()


__starting_point()
