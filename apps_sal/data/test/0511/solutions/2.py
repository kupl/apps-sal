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
# from fractions import gcd
# x, y = map(int, input().split())
#
# a = int(x**.5 + 1)
# p = []
# x1 = x
# for i in range(2, a + 1):
#   if (x1 % i == 0):
#     p.append(i)
#     while (x1 % i == 0):
#       x1 //= i
# if (x1 > 1):
#   p.append(x1)
# ans = 0
# while (y != 0):
#   r = gcd(x, y)
#   x //= r
#   y //= r
#   max_can = 0
#   for i in range(len(p)):
#     if (x % p[i] == 0):
#       max_can = max(max_can, y - y % p[i])
#   ans += y - max_can
#   y = max_can
# print(ans)

