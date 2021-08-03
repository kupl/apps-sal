from itertools import combinations, permutations, combinations_with_replacement

n, k = [int(i) for i in input().split()]

keys = list(range(n))


def fac(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def comb(n, k):
    return fac(n) / (fac(n - k) * fac(k))


c = 0
for i in range(1, k + 1):
    if(i == 1):
        c += 1
    if(i == 2):
        c += comb(n, n - i)
    if(i == 3):
        c += comb(n, n - i) * 2
    if(i == 4):
        c += comb(n, n - i) * 9

print(int(c))
