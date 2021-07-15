import math
from collections import Counter
import itertools
from math import sqrt

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

s,p = mi()

for i in range(1,1000010):
    if i*(s-i) == p:
        print("Yes")
        return
print("No")
