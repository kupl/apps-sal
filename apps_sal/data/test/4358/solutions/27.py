import math
import collections
from itertools import product

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n = ii()
p = [ii() for i in range(n)]
p.sort()
p[-1] //= 2
print(sum(p))
