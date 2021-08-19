from functools import lru_cache
from itertools import accumulate
from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop, heapify
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline
M = mod = 998244353


def factors(n):
    return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def inv_mod(n):
    return pow(n, mod - 2, mod)


def li():
    return [int(i) for i in input().rstrip('\n').split()]


def st():
    return input().rstrip('\n')


def val():
    return int(input().rstrip('\n'))


def li2():
    return [i for i in input().rstrip('\n')]


def li3():
    return [int(i) for i in input().rstrip('\n')]


def isprime(n):
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return 0
    return 1


for _ in range(val()):
    n = val()
    l1 = factors(n)[1:]
    l = []
    for j in l1:
        if isprime(j):
            l.append(j)
    l1 = set(l1)
    l1 -= set(l)
    d = defaultdict(set)
    for j in range(len(l)):
        for i in sorted(list(l1)):
            if i % l[j] == 0 and i % l[j - 1] == 0:
                d[tuple(sorted([l[j], l[j - 1]]))].add(i)
                l1.remove(i)
                break
    for j in range(len(l)):
        for i in sorted(list(l1)):
            if i % l[j] == 0 and i % l[j - 1] == 0:
                d[tuple(sorted([l[j], l[j - 1]]))].add(i)
                l1.remove(i)
    only = defaultdict(list)
    for j in range(len(l)):
        for i in sorted(list(l1)):
            if i % l[j] == 0:
                only[l[j]].append(i)
                l1.remove(i)
    fin = []
    if len(l) == 2:
        fin.append(l[0])
        for j in only[l[0]]:
            fin.append(j)
        for i in range(len(l)):
            for j in list(d[tuple(sorted([l[i], l[(i + 1) % len(l)]]))]):
                fin.append(j)
                d[tuple(sorted([l[i], l[(i + 1) % len(l)]]))].remove(j)
                if i != len(l) - 1:
                    break
            if i != len(l) - 1:
                fin.append(l[i + 1])
                for j in only[l[i + 1]]:
                    fin.append(j)
    else:
        fin.append(l[0])
        for j in only[l[0]]:
            fin.append(j)
        for i in range(len(l)):
            for j in d[tuple(sorted([l[i], l[(i + 1) % len(l)]]))]:
                fin.append(j)
            if i != len(l) - 1:
                fin.append(l[i + 1])
                for j in only[l[i + 1]]:
                    fin.append(j)
    ans = 0
    for i in range(len(fin)):
        if math.gcd(fin[i], fin[i - 1]) == 1:
            ans += 1
    print(*fin)
    print(ans)
