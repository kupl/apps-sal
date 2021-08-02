# from itertools import combinations
# from bisect import bisect_left
# from functools import *
# from collections import namedtuple
def I(): return list(map(int, input().split()))


a = sorted(I())
print(max(0, a[2] - a[1] - a[0] + 1))
