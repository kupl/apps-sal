from functools import reduce
from operator import *
from math import *
from sys import *
from string import *
setrecursionlimit(10**7)
def RI(): return list(map(int, input().split()))
def RS(): return input().rstrip().split()


#################################################
n, m = RI()
ans = 0
while m:
    ans += n // m
    n, m = m, n % m
print(ans)
