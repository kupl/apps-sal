import sys
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
def mi(): return list(map(int, input().rstrip().split()))
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


def __starting_point():

    # write code
    n, a, x, b, y = mi()
    while (a % n != x % n and b % n != y % n):
        a += 1
        a %= n
        b -= 1
        b %= n
        if a % n == b % n:
            print('YES')
            break
    else:
        print('NO')

__starting_point()
