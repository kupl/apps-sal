import math
from collections import Counter
from itertools import product

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

k,x = mi()

if 500*k >= x:
    print("Yes")
else:
    print("No")
