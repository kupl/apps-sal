# using main() makes code faster from the point of view of "access to variables in nonlocal name-space"
# def main():

# for i, a in enumerate(iterable)
# q, mod = divmod(a, b)
# divmod(x, y) returns the tuple (x//y, x%y)
# manage median(s) using two heapq https://atcoder.jp/contests/abc127/tasks/abc127_f
import sys
sys.setrecursionlimit(10**7)
from itertools import accumulate, combinations, permutations # https://docs.python.org/ja/3/library/itertools.html
from math import factorial
def factorize(n):
    """return the factors of the Arg and count of each factor
    
    Args:
        n (long): number to be resolved into factors
    
    Returns:
        list of tuples: factorize(220) returns [(2, 2), (5, 1), (11, 1)]
    """
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
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
    # TODO: How should I do when n - r is negative?
    if n < 0 or r < 0:
        raise Exception('combinations_count(n, r) not defined when n or r is negative')
    if n - r < r: r = n - r
    if r < 0: return 0
    if r == 0: return 1
    if r == 1: return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
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
from collections import deque, Counter, defaultdict # https://docs.python.org/ja/3/library/collections.html#collections.deque
from heapq import heapify, heappop, heappush, heappushpop, heapreplace,nlargest,nsmallest # https://docs.python.org/ja/3/library/heapq.html
from copy import deepcopy, copy # https://docs.python.org/ja/3/library/copy.html
from operator import itemgetter
# ex1: List.sort(key=itemgetter(1))
# ex2: sorted(tuples, key=itemgetter(1,2))
from functools import reduce
from fractions import gcd # Deprecated since version 3.5: Use math.gcd() instead.
def gcds(numbers):
    return reduce(gcd, numbers)
def lcm(x, y):
    return (x * y) // gcd(x, y)
def lcms(numbers):
    return reduce(lcm, numbers, 1)

# first create factorial_list
# fac_list = mod_factorial_list(n)
INF = 10 ** 18
MOD = 10 ** 9 + 7
modpow = lambda a, n, p = MOD: pow(a, n, p) # Recursive function in python is slow!
def modinv(a, p = MOD):
    # evaluate reciprocal using Fermat's little theorem:
    # a**(p-1) is identical to 1 (mod p) when a and p is coprime
    return modpow(a, p-2, p)
def modinv_list(n, p = MOD):
    if n <= 1:
        return [0,1][:n+1]
    else:
        inv_t = [0,1]
        for i in range(2, n+1):
            inv_t += [inv_t[p % i] * (p - int(p / i)) % p]
        return inv_t
def modfactorial_list(n, p = MOD):
    if n == 0:
        return [1]
    else:
        l = [0] * (n+1)
        tmp = 1
        for i in range(1, n+1):
            tmp = tmp * i % p
            l[i] = tmp
        return l
def modcomb(n, k, fac_list = [], p = MOD):
    # fac_list = modfactorial_list(100)
    # print(modcomb(100, 5, modfactorial_list(100)))
    from math import factorial
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    if len(fac_list) <= n:
        a = factorial(n) % p
        b = factorial(k) % p
        c = factorial(n-k) % p
    else:
        a = fac_list[n]
        b = fac_list[k]
        c = fac_list[n-k]
    return (a * modpow(b, p-2, p) * modpow(c, p-2, p)) % p
def modadd(a, b, p = MOD):
    return (a + b) % MOD
def modsub(a, b, p = MOD):
    return (a - b) % p
def modmul(a, b, p = MOD):
    return ((a % p) * (b % p)) % p
def moddiv(a, b, p = MOD):
    return modmul(a, modpow(b, p-2, p))

# initialize variables and set inputs
# initialize variables
    # to initialize list, use [0] * n
    # to initialize two dimentional array, use [[0] * N for _ in range(N)]
# set inputs
    # open(0).read() is a convenient method:
    # ex) n, m, *x = map(int, open(0).read().split())
    #     min(x[::2]) - max(x[1::2])
    # ex2) *x, = map(int, open(0).read().split())
    #     don't forget to add comma after *x if only one variable is used
# preprocessing
    # transpose = [x for x in zip(*data)]
    # ex) [[1, 2, 3], [4, 5, 6], [7, 8, 9]] => [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# calculate and output
    # output pattern
    # ex1) print(*l) => when l = [2, 5, 6], printed 2 5 6

# functions used
r = lambda: sys.stdin.readline().strip()
r_int = lambda: int(r())
R = lambda: list(map(int, r().split()))
Rfloat = lambda: list(map(float, r().split()))
Rtuple = lambda: tuple(map(int, r().split()))
Rmap = lambda: list(map(int, r().split()))
# single int: int(r())
# single string: r()
# single float: float(r())
# line int: R()
# line string: r().split()
# line (str, int, int): [j if i == 0 else int(j) for i, j in enumerate(r().split())]
# lines int: [R() for _ in range(n)]

# set inputs
# sys.stdin = open('sample.txt') # for test
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

# def __starting_point():
#     main()

__starting_point()
