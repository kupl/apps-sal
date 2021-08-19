from math import gcd


def popcnt(n):
    return bin(n).count("1") % 2


def calc(gen, limit):
    divisors = []
    i = 2
    gen_copy = gen
    while gen > 1 and i * i <= gen_copy:
        if gen % i == 0:
            divisors.append(i)
            while gen % i == 0:
                gen //= i
        i += 1
    if gen != 1:
        divisors.append(gen)
    # print(divisors)

    l = len(divisors)
    res = 0
    for bit in range(1 << l):
        prod = 1
        for j, div in enumerate(divisors):
            if (bit >> j) & 1:
                prod *= div
        #print(bit, prod)
        if popcnt(bit):
            res -= (limit - 1) // prod
        else:
            res += (limit - 1) // prod
    return res


T = int(input())
for _ in range(T):
    a, m = map(int, input().split())
    g = gcd(a, m)
    k, l = a // g, m // g
    print(calc(l, l + k) - calc(l, k))
