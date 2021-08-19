import sys


def fact(n):
    ret = 1
    for x in range(1, n + 1):
        ret = ret * x
    return ret


def C(n, k):
    return fact(n) // (fact(k) * fact(n - k))


def get(n, pos):
    while pos > 0:
        n //= 10
        pos -= 1
    return n % 10


n = int(input())
k = get(n, 4)
k = k * 10 + get(n, 2)
k = k * 10 + get(n, 0)
k = k * 10 + get(n, 1)
k = k * 10 + get(n, 3)
k = k ** 5
q = k % 100000
a = []
for x in range(5):
    a.append(q % 10)
    q //= 10
for x in reversed(a):
    print(x, end='')
