from math import sqrt
n, b = [int(i) for i in input().split()]


def geg(n, k, l):
    if k <= n:
        return n // k + geg(n, k * l, l)
    else:
        return 0


def fact(b, n):
    D = {}
    for i in range(2, round(sqrt(b)) + 1):
        if b % i == 0:
            s = 0
            while b % i == 0:
                b = b // i
                s += 1
            D[i] = s
    L = []
    for i in list(D.keys()):
        L.append(geg(n, i, i) // D[i])
    if b != 1:
        L.append(geg(n, b, b))
    m = L[0]
    for i in L:
        if m > i:
            m = i
    return m


print(fact(b, n))
