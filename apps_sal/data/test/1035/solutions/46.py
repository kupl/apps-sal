
import math


def gcd(a, b):
    while b > 0:
        tmp = b
        b = a % b
        a = tmp
    return a


def count_prime_factorize(n):
    res = 1
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            res += 1
            while n % i == 0:
                n //= i
        i += 1
    if n != 1:
        res += 1
    return res


a, b = list(map(int, input().strip().split()))
x = gcd(a, b)
res = count_prime_factorize(x)
print(res)
