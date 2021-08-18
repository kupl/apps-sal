
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest
from collections import deque, Counter, defaultdict
from fractions import gcd
from functools import reduce
from operator import itemgetter
from copy import deepcopy, copy
from math import factorial
from itertools import accumulate, combinations, permutations
import sys
sys.setrecursionlimit(10**7)


def factorize(n):
    """return the factors of the Arg and count of each factor

    Args:
        n (long): number to be resolved into factors

    Returns:
        list of tuples: factorize(220) returns [(2, 2), (5, 1), (11, 1)]
    """
    fct = []
    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def combinations_count(n, r):
    """Return the number of selecting r pieces of items from n kinds of items.

    Args:
        n (long): number
        r (long): number

    Raises:
        Exception: not defined when n or r is negative

    Returns:
        long: number
    """
    if n < 0 or r < 0:
        raise Exception('combinations_count(n, r) not defined when n or r is negative')
    if n - r < r:
        r = n - r
    if r < 0:
        return 0
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result


def combinations_with_replacement_count(n, r):
    """Return the number of selecting r pieces of items from n kinds of items allowing individual elements to be repeated more than once.

    Args:
        n (long): number
        r (long): number

    Raises:
        Exception: not defined when n or r is negative

    Returns:
        long: number
    """
    if n < 0 or r < 0:
        raise Exception('combinations_with_replacement_count(n, r) not defined when n or r is negative')
    elif n == 0:
        return 1
    else:
        return combinations_count(n + r - 1, r)


def gcds(numbers):
    return reduce(gcd, numbers)


def lcm(x, y):
    return (x * y) // gcd(x, y)


def lcms(numbers):
    return reduce(lcm, numbers, 1)


INF = 10 ** 18
MOD = 10 ** 9 + 7
def modpow(a, n, p=MOD): return pow(a, n, p)


def modinv(a, p=MOD):
    return modpow(a, p - 2, p)


def modinv_list(n, p=MOD):
    if n <= 1:
        return [0, 1][:n + 1]
    else:
        inv_t = [0, 1]
        for i in range(2, n + 1):
            inv_t += [inv_t[p % i] * (p - int(p / i)) % p]
        return inv_t


def modfactorial_list(n, p=MOD):
    if n == 0:
        return [1]
    else:
        l = [0] * (n + 1)
        tmp = 1
        for i in range(1, n + 1):
            tmp = tmp * i % p
            l[i] = tmp
        return l


def modcomb(n, k, fac_list=[], p=MOD):
    from math import factorial
    if n < 0 or k < 0 or n < k:
        return 0
    if n == 0 or k == 0:
        return 1
    if len(fac_list) <= n:
        a = factorial(n) % p
        b = factorial(k) % p
        c = factorial(n - k) % p
    else:
        a = fac_list[n]
        b = fac_list[k]
        c = fac_list[n - k]
    return (a * modpow(b, p - 2, p) * modpow(c, p - 2, p)) % p


def modadd(a, b, p=MOD):
    return (a + b) % MOD


def modsub(a, b, p=MOD):
    return (a - b) % p


def modmul(a, b, p=MOD):
    return ((a % p) * (b % p)) % p


def moddiv(a, b, p=MOD):
    return modmul(a, modpow(b, p - 2, p))


def r(): return sys.stdin.readline().strip()
def r_int(): return int(r())
def R(): return list(map(int, r().split()))
def Rfloat(): return list(map(float, r().split()))
def Rtuple(): return tuple(map(int, r().split()))
def Rmap(): return list(map(int, r().split()))


N = r_int()
Dic = defaultdict(list)
V = 10**5 + 5
Arrived = [False] * (2 * V)
for _ in range(N):
    x, y = R()
    y += V
    Dic[x].append(y)
    Dic[y].append(x)

ans = 0
task = []
for k, v in list(Dic.items()):
    if Arrived[k]:
        continue
    Arrived[k] = True
    cntx = 0
    cnty = 0
    if k < V:
        cntx += 1
    else:
        cnty += 1
    cntdot = 0
    task.extend(v)
    cntdot += len(v)
    while task:
        s = task.pop()
        if Arrived[s]:
            continue
        if s < V:
            cntx += 1
        else:
            cnty += 1
        Arrived[s] = True
        task.extend(Dic[s])
        cntdot += len(Dic[s])
    ans += cntx * cnty - cntdot // 2
print(ans)


__starting_point()
