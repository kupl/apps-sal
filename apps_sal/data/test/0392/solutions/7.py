from itertools import accumulate, chain, cycle
n = int(input())


def prime_powers_iter(n):
    for c in accumulate(chain([2, 1, 2], cycle([2, 4]))):
        if c * c > n: break
        if n % c: continue
        d, p = (), c
        while not n % c:
            n, p, d = n // c, p * c, d + (p,)
        yield(d)
    if n > 1: yield((n,))


def prime_powers(n):
    return list(i[0] for i in list(prime_powers_iter(n)))


mul = 1
for i in prime_powers(n):
    mul *= i
print(mul)
