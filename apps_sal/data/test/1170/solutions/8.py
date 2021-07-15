import time
import itertools

import math

x = 10**9+2



def find_factor(x):
    k = int(math.ceil(math.sqrt(x)))
    if x//k == k:
        k -=1
    for i in range(k,2,-1):
        if not x%i:
            yield i
    yield 1

def find_factor_div2(x):
    k = int((math.ceil(math.sqrt(x))//2)*2)
    if x//k == k:
        k -=2
    for i in range(k, 1, -2):
        if not x%i and not (x//i)%2:
            yield i
    return 0

def _sol_kMn_kPn_for_x(x):

    if x%4 == 0:
        f = find_factor_div2(x)
        if f:
            for k in f:
                yield k, x/k
        return 0
    if x%2 == 0:
        return 0
    f = find_factor(x)
    if f:
        for k in f:

            yield k, x/k
    return 0


def sol_k_n_for_x(x):
    if x < 4:
        if x == 3:
            yield (1, 2)
        elif x == 0:
            yield (1, 1)
        else:
            return 0
        return

    k_n = _sol_kMn_kPn_for_x(x)

    if not k_n:
        return 0
    for _k, _n in k_n:
        n, k =  ((_n - _k)//2, (_k + _n)//2)

        yield n,k


def sol_m_n(x):

    if x == 0:
        return (1, 1)

    kn = sol_k_n_for_x(x)

    if not kn:
        return -1, -1
    for k, n in kn:
        l = math.ceil((n+1)/(k+1))
        r = math.floor((n)/(k))
    #if l == (n+1)/(k+1):
     #   l +=1

        if l <= r:
            return r, n
    return -1,-1


def __starting_point():
    n = int(input())

    for i in range(n):
        q = int(input())
        m, n = sol_m_n(q)
        if m == -1:
            print(-1)
        else:
            print(int(n), int(m))

# 5, 8

__starting_point()
