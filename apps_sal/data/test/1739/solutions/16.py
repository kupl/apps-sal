from bisect import bisect_left
import math
from itertools import permutations
import sys
'\n\nPPPPPPP       RRRRRRR\t\t    OOOO\t  VV        VV    EEEEEEEEEE\nPPPPPPPP      RRRRRRRR         OOOOOO     VV       VV\t  EE\nPPPPPPPPP     RRRRRRRRR       OOOOOOOO    VV      VV\t  EE\nPPPPPPPP      RRRRRRRR        OOOOOOOO    VV     VV    \t  EEEEEE\nPPPPPPP       RRRRRRR         OOOOOOOO    VV    VV        EEEEEEE\nPP  \t\t  RRRR\t\t\t  OOOOOOOO    VV   VV         EEEEEE\nPP\t\t\t  RR  RR          OOOOOOOO    VV  VV          EE\nPP\t\t\t  RR    RR         OOOOOO     VV VV           EE\nPP\t\t\t  RR      RR        OOOO      VVVV            EEEEEEEEEE\n\n'
'\n Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away.\n'
input = sys.stdin.readline


def ceil(x):
    if x != int(x):
        x = int(x) + 1
    return x


def factorial(x, m):
    val = 1
    while x > 0:
        val = val * x % m
        x -= 1
    return val


def fact(x):
    val = 1
    while x > 0:
        val *= x
        x -= 1
    return val


def swaparr(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def nCr(n, k):
    if k > n:
        return 0
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return int(res)


def upper_bound(a, x, lo=0, hi=None):
    if hi == None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def primefs(n):
    primes = {}
    while n % 2 == 0 and n > 0:
        primes[2] = primes.get(2, 0) + 1
        n = n // 2
    for i in range(3, int(n ** 0.5) + 2, 2):
        while n % i == 0 and n > 0:
            primes[i] = primes.get(i, 0) + 1
            n = n // i
    if n > 2:
        primes[n] = primes.get(n, 0) + 1
    return primes


def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if y & 1 == 1:
            res = res * x % p
        y = y >> 1
        x = x * x % p
    return res


def swap(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)


def find(x, link):
    p = x
    while p != link[p]:
        p = link[p]
    while x != p:
        nex = link[x]
        link[x] = p
        x = nex
    return p


def union(x, y, link, size):
    x = find(x, link)
    y = find(y, link)
    if size[x] < size[y]:
        (x, y) = swap(x, y)
    if x != y:
        size[x] += size[y]
        link[y] = x


def sieve(n):
    prime = [True for i in range(n + 1)]
    (prime[0], prime[1]) = (False, False)
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime


def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result = result * (1.0 - 1.0 / float(p))
        p = p + 1
    if n > 1:
        result = result * (1.0 - 1.0 / float(n))
    return int(result)


def is_prime(n):
    if n == 0:
        return False
    if n == 1:
        return True
    for i in range(2, int(n ** (1 / 2)) + 1):
        if not n % i:
            return False
    return True


MAXN = int(100000.0 + 5)


def spf_sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2
    for i in range(3, ceil(MAXN ** 0.5), 2):
        if spf[i] == i:
            for j in range(i * i, MAXN, i):
                if spf[j] == j:
                    spf[j] = i


spf = [0 for i in range(MAXN)]


def factoriazation(x):
    res = []
    for i in range(2, int(x ** 0.5) + 1):
        while x % i == 0:
            res.append(i)
            x //= i
    if x != 1:
        res.append(x)
    return res


def factors(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)
    return list(set(res))


def int_array():
    return list(map(int, input().strip().split()))


def float_array():
    return list(map(float, input().strip().split()))


def str_array():
    return input().strip().split()


MOD = int(1000000000.0) + 7
CMOD = 998244353
INF = float('inf')
NINF = -float('inf')


def solve():
    (n, x) = list(map(int, input().split()))
    powers = list(map(int, input().split()))
    summ = sum(powers)
    biggest = max(powers)
    p = summ - biggest
    number_of_powers = powers.count(biggest)
    while number_of_powers % x == 0:
        biggest -= 1
        p += 1
        number_of_powers = number_of_powers // x + powers.count(biggest)
    if p > summ:
        p = summ
    print(pow(x, p, MOD))


def __starting_point():
    for _ in range(1):
        solve()


__starting_point()
