# from itertools import combinations
# from bisect import bisect_left
# from functools import *
# from collections import Set

I = lambda: list(map(int, input().split()))
n, k = I()
a = sorted(I())
b = set(a)
if k != 1:
    for i in a:
        if i in b:
            b.discard(i * k)
print(len(b))
