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
    n, m, ta, tb, k = mi()
    a = lmi()
    b = lmi()
    if n <= k or m <= k:
        print(-1)
        return
    a = [i + ta for i in a]
    lenb = len(b)
    a.sort()
    b.sort()
    # print(a)
    ans = -10**9
    for i in range(k + 1):
        # print(b[bisect_left(b, a[i]) + (k - i)])
        if bisect_left(b, a[i]) + (k - i) >= lenb:
            print(-1)
            return
        else:
            ans = max(ans, b[bisect_left(b, a[i]) + (k - i)])
    print(ans + tb)


__starting_point()
