from sys import stdin
from collections import Counter, deque, defaultdict, OrderedDict, namedtuple
from bisect import bisect_left, bisect_right, insort
from math import sqrt, ceil, floor, factorial, gcd
from heapq import heapify, heappush, heappop, heappushpop, heapreplace, merge, nlargest, nsmallest
from itertools import permutations, combinations

mod = 10**9 + 7
inf = float('inf')
negin = float('-inf')
a_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
AZ = dict(list(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', list(range(1, 27)))))


def b_search(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return(i)
    else:
        return(-1)


def opt_sieve(n):
    prime = []
    is_prime = [True for i in range(n)]
    spf = [0 for i in range(n)]
    is_prime[0] = is_prime[1] = False
    for i in range(2, n):
        if is_prime[i]:
            spf[i] = i
            prime.append(i)
        j = 0
        while j < len(prime) and i * prime[j] < n and prime[j] <= spf[i]:
            is_prime[i * prime[j]] = False
            spf[i * prime[j]] = prime[j]
            j += 1
    return is_prime


is_prime = opt_sieve(1000001)

t = int(stdin.readline())
while t:
    s = input()
    if s[len(s) - 2:] == 'po':
        print('FILIPINO')
    elif s[len(s) - 4:] == 'desu' or s[len(s) - 4:] == 'masu':
        print('JAPANESE')
    elif s[len(s) - 5:] == 'mnida':
        print('KOREAN')

    t -= 1
