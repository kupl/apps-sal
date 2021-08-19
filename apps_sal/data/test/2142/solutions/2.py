import random


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b / gcd(a, b)


for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f = -1
    a.sort()
    b.sort()
    d = {}
    for i in a:
        d[i] = 1
    for i in b:
        if i in d:
            f = i
    if f == -1:
        print('NO')
    else:
        print('YES')
        print(1, f)
