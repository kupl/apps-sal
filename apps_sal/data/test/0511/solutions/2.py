import sys
import math
from fractions import gcd


def prime_factors(n):
    res = []
    if n % 2 == 0:
        res.append(2)
    while n % 2 == 0:
        n //= 2
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            res.append(i)
        while n % i == 0:
            n //= i
    if n > 2:
        res.append(n)
    return res


def main():
    a, b = list(map(int, sys.stdin.readline().split()))
    r = prime_factors(a)
    ans = 0
    while b > 1:
        g = gcd(a, b)
        b //= g
        a //= g
        v = 0
        for i in range(len(r)):
            if (a % r[i] == 0):
                v = max(v, b - b % r[i])
        ans += b - v
        b = v

    if b == 1:
        ans += 1

    print(ans)


main()
