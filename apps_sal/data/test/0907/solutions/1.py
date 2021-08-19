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
    n, m = mi()
    l = [0] * m
    r = [0] * m
    for i in range(m):
        l[i], r[i] = mi()
    lf = l[0]
    rf = r[0]
    flag = True
    for i in range(m):
        if l[i] != lf and r[i] != lf:
            if l[i] != rf and r[i] != rf:
                lf2 = l[i]
                rf2 = r[i]
                flag = False
                break
    if flag:
        print('YES')
        return
    Lis = [lf, rf, lf2, rf2]
    for i in range(3):
        for j in range(i + 1, 4):
            left = Lis[i]
            right = Lis[j]
            for cnt in range(m):
                if l[cnt] != left and r[cnt] != left:
                    if l[cnt] != right and r[cnt] != right:
                        break
            else:
                print('YES')
                return
    print('NO')


__starting_point()
