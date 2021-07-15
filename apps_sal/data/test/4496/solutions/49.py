import math
import collections
from itertools import product

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

d = ii()
if d == 25:
    print("Christmas")
elif d == 24:
    print("Christmas Eve")
elif d == 23:
    print("Christmas Eve Eve")
elif d == 22:
    print("Christmas Eve Eve Eve")
