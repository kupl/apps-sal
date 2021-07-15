import math
from collections import Counter
from itertools import product

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

a,b,k = mi()

if a <= k:
    print(0,max(0,b-(k-a)))
else:
    print(a-k,b)
