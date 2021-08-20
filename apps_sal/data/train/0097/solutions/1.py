import heapq
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline
M = mod = 10 ** 9 + 7


def factors(n):
    return sorted(list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))))


def inv_mod(n):
    return pow(n, mod - 2, mod)


def li():
    return [int(i) for i in input().rstrip('\n').split(' ')]


def st():
    return input().rstrip('\n')


def val():
    return int(input())


def li2():
    return [i for i in input().rstrip('\n').split(' ')]


n = val()
for _ in range(n):
    (s1, s2) = li2()
    fin = sorted(s1)
    if fin[0] > s2[0]:
        print('---')
        continue
    for i in range(len(s1)):
        if s1[i] != fin[i]:
            for j in range(len(s1) - 1, -1, -1):
                if s1[j] == fin[i]:
                    s1 = list(s1)
                    s1[j] = s1[i]
                    s1[i] = fin[i]
                    s1 = ''.join(s1)
                    break
            break
    print('---' if s1 >= s2 else s1)
