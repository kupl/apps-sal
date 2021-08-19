import sys
# gcd
# from fractions import gcd
# from math import ceil, floor
# from copy import deepcopy
from itertools import accumulate
# l = ['a', 'b', 'b', 'c', 'b', 'a', 'c', 'c', 'b', 'c', 'b', 'a']
# S = Counter(l)  # make Counter Class
# print(S.most_common(2))  # [('b', 5), ('c', 4)]
# print(S.keys())  # dict_keys(['a', 'b', 'c'])
# print(S.values())  # dict_values([3, 5, 4])
# print(S.items())  # dict_items([('a', 3), ('b', 5), ('c', 4)])
# from collections import Counter
# import math
# from functools import reduce
#
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return list(map(int, input().rstrip().split()))
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


n, m, r = mi()
s = lmi()
b = lmi()
s.sort()
b.sort()
b.reverse()
a = s[0]
z = b[0]

print(max(r + (z - a) * (r // a), r))
