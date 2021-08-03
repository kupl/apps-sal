import sys
from bisect import bisect_left
# gcd
# from fractions import gcd
# from math import ceil, floor
# from copy import deepcopy
# from itertools import accumulate
# l = ['a', 'b', 'b', 'c', 'b', 'a', 'c', 'c', 'b', 'c', 'b', 'a']
# print(S.most_common(2))  # [('b', 5), ('c', 4)]
# print(S.keys())  # dict_keys(['a', 'b', 'c'])
# print(S.values())  # dict_values([3, 5, 4])
# print(S.items())  # dict_items([('a', 3), ('b', 5), ('c', 4)])
# from collections import Counter
# import math
# from functools import reduce
#
# fin = open('in_1.txt', 'r')
# sys.stdin = fin
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


def __starting_point():

    # write code
    n = ii()
    cnta = 0
    cntb = 0
    lista = []
    listb = []
    for i in range(n):
        a, b = mi()
        if a > b:
            cntb += 1
            listb.append((a, b, i + 1))
        else:
            cnta += 1
            lista.append((a, b, i + 1))
    if cnta >= cntb:
        lista.sort(key=lambda x: x[0], reverse=True)
        print(len(lista))
        for i in lista:
            print(i[2], end=" ")
        print()
    else:
        listb.sort(key=lambda x: x[1])
        print(len(listb))
        for i in listb:
            print(i[2], end=" ")
        print()


__starting_point()
