from math import gcd, sqrt
from functools import reduce

n, *A = map(int, open(0).read().split())
def f(A):
    sup = max(A)+1
    table = [i for i in range(sup)]
    for i in range(2, int(sqrt(sup))+1):
        if table[i] == i:
            for j in range(i**2, sup, i):
                table[j] = i

    D = set()
    for a in A:
        while a != 1:
            if a not in D:
                D.add(a)
                a //= table[a]
            else:
                return False
    return True

if reduce(gcd, A) == 1:
    if f(A):
        print('pairwise coprime')
    else:
        print('setwise coprime')
else:
    print('not coprime')
