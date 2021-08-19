import sys


def input():
    return sys.stdin.readline()[:-1]


(n, m, q) = list(map(int, input().split()))


def gcd(a, b):
    (a, b) = (max(a, b), min(a, b))
    while a % b != 0:
        (a, b) = (b, a % b)
    return b


g = gcd(n, m)
for i in range(q):
    (s1, s2, e1, e2) = list(map(int, input().split()))
    if s1 == 1:
        scheck = n // g
    else:
        scheck = m // g
    if e1 == 1:
        echeck = n // g
    else:
        echeck = m // g
    if (s2 - 1) // scheck == (e2 - 1) // echeck:
        print('YES')
    else:
        print('NO')
