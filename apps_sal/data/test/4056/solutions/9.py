from sys import stdin, stdout

input = stdin.readline


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def divisors(x):
    res = 0
    d = 1
    while d * d <= x:
        if x % d == 0:
            res += 1
            res += (d != x / d)
        d += 1

    return res


n = int(input())
a = [int(i) for i in input().split()]
nwd = 0
for i in a:
    nwd = gcd(nwd, i)

print(divisors(nwd))
